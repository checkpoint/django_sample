from django.conf.urls import url

from . import views

urlpatterns = [

    # hello world
    url(r'^$', views.index, name='index'),

    # blog
    url(r'^(?P<blog_id>[0-9]+)/$', views.articles, name='articles'),

    # article
    url(r'^(?P<blog_id>[0-9]+)/new/$', views.new_article, name='new_article'),
    url(r'^(?P<blog_id>[0-9]+)/article/(?P<article_id>[0-9]+)/edit/$', views.edit_article, name='edit_article'),
    url(r'^(?P<blog_id>[0-9]+)/article/(?P<article_id>[0-9]+)/delete/$', views.delete_article, name='delete_article'),

]
