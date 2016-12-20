# -*- encoding:utf-8 -*-


from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import ArticleForm, ArticleDeleteForm
from .models import Article, Blog


def index(request):
    return HttpResponse('Hello Django!!')


def articles(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    article_list = Article.objects.filter(blog_id=blog_id).order_by('-created_at')[:10]

    template = loader.get_template('article/list.html')
    context = {
        'blog': blog,
        'articles': article_list,
    }
    return HttpResponse(template.render(context, request=request))


def new_article(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.blog_id = blog.id
            article.save()
            return HttpResponseRedirect(reverse('articles', args=[blog_id]))

    else:
        form = ArticleForm()

    template = loader.get_template('article/new.html')
    context = {
        'form': form,
        'blog': blog,
    }
    return HttpResponse(template.render(context, request=request))


def edit_article(request, blog_id, article_id):
    article = Article.objects.get(blog_id=blog_id, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return HttpResponseRedirect(reverse('articles', args=[blog_id]))
    else:
        form = ArticleForm(instance=article)
    template = loader.get_template('article/edit.html')
    context = {
        'form': form,
        'blog': article.blog,
        'article': article,
    }
    return HttpResponse(template.render(context, request=request))


def delete_article(request, blog_id, article_id):
    article = Article.objects.get(blog_id=blog_id, id=article_id)
    form = ArticleDeleteForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.delete()
        return HttpResponseRedirect(reverse('articles', args=[blog_id]))
