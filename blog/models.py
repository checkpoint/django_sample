# -*- encoding:utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    class Meta:
        db_table = 'blog'

    user = models.ForeignKey(
        User
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(

    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('言語', '言語'),
        ('フレームワーク', 'フレームワーク'),
        ('開発プロセス', '開発プロセス'),
        ('データベース', 'データベース'),
        ('ツール', 'ツール'),
        ('勉強会', '勉強会'),
    )

    class Meta:
        db_table = 'article'

    blog = models.ForeignKey(
        Blog
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(

    )

    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES[0][0]
    )

    is_draft = models.BooleanField(
        default=False
    )

    pub_date = models.DateTimeField(
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
