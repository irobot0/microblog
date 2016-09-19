from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView

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