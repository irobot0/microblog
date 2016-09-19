from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status=Post.STATUS_PUBLISHED)


class Post(models.Model):

    objects = models.Manager()
    published = PublishedManager()

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='published_time')
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    body = models.TextField()
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default=STATUS_DRAFT)

    class Meta:
        ordering = ('-published_time',)

    def __str__(self):
        return self.title

    '''
    Returns the canonical URL of the object.
    '''
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.published_time.year,
                           self.published_time.strftime('%m'),
                           self.published_time.strftime('%d'),
                           self.slug
                       ])
