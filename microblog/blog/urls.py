from django.conf.urls import url
from . import views

urlpatterns = [
    # a list of posts. e.g. /blog/
    url(r'^$', views.post_list, name='post_list'),

    # detail of a post. e.g. /blog/2016/09-19/who-was-django-reinhardt/
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]