from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
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
                              default=DRAFT)

    class Meta:
        ordering = ('-published_time',)

    def __str__(self):
        return self.title

