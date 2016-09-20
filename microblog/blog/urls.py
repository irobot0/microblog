from django.conf.urls import url
from . import views

urlpatterns = [
    # a list of posts. e.g. /blog/
    url(r'^$', views.PostListView.as_view(), name='post_list'),

    # detail of a post. e.g. /blog/2016/09-19/who-was-django-reinhardt/
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

    # Share a post via email. e.g. /blog/2/share/
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]