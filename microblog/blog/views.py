from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status=Post.STATUS_PUBLISHED,
                             published_time__year=year,
                             published_time__month=month,
                             published_time__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})