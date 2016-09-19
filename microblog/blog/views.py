from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post


def post_list(request):
    published_posts = Post.published.all()
    # Display 3 posts in each page.
    paginator = Paginator(published_posts, 3)
    page_num = request.GET.get('page')
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        # Deliver the first page when the argument is not an integer.
        page = paginator.page(1)
    except EmptyPage:
        # Deliver the last page when the argument is out of range.
        page = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status=Post.STATUS_PUBLISHED,
                             published_time__year=year,
                             published_time__month=month,
                             published_time__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})