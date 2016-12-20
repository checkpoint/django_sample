from django.contrib import admin

from .models import Article
from .models import Blog

admin.site.register(Blog)
admin.site.register(Article)
