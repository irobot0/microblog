# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published_time')),
                ('body', models.TextField()),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='blog_posts')),
            ],
            options={
                'ordering': ('-published_time',),
            },
        ),
    ]
