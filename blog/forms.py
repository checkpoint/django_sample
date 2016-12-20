from django.forms import ModelForm

from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'pub_date', 'is_draft', 'category']


class ArticleDeleteForm(ModelForm):
    class Meta:
        model = Article
        fields = ['id']
