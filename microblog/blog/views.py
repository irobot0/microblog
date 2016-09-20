from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from smtplib import SMTPException

from .forms import EmailPostForm
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'page'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status=Post.STATUS_PUBLISHED,
                             published_time__year=year,
                             published_time__month=month,
                             published_time__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


def mail_delivered(subject, message, sender, receivers):
    try:
        send_mail(subject, message, sender, receivers, fail_silently=False)
    except SMTPException:
        return False
    else:
        return True


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.STATUS_PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(
                form_data['name'], form_data['email'], post.title
            )
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                post.title, post_url, form_data['name'], form_data['review']
            )
            sender = settings.EMAIL_HOST_USER
            receivers = [form_data['to']]
            if mail_delivered(subject, message, sender, receivers):
                print('mail is delivered')
                template = 'blog/post/share_sent_succeed.html'
                context = {
                    'post': post,
                    'form_data': form_data,
                }
                return render(request, template, context)
            else:
                print('mail not delivered')
                template = 'blog/post/share_sent_failed.html'
                context = {
                    'post': post,
                    'form': form,
                    'error_msg': 'SMTPException',
                }
                return render(request, template, context)
        else:
            template = 'blog/post/share_to_send.html'
            context = {
                'post': post,
                'form': form,
            }
            return render(request, template, context)
    else:
        template = 'blog/post/share_to_send.html'
        form = EmailPostForm()
        context = {
            'post': post,
            'form': form,
        }
        return render(request, template, context)
