from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        article_data = []
        all_article = Article.objects.all().order_by('-created_date')[:9]

        for article in all_article:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'created_date': article.created_date,
                'author': article.author,
                'category': article.category,
            })
        context = {
            'article_data': article_data
        }
        return render(request, 'index.html', context)
