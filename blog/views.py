from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        # all articles
        article_data = []
        all_article = Article.objects.all().order_by('-created_date')
        for article in all_article:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'author': article.author,
                'created_date': article.created_date,
                'category': article.category,
            })

        # promoted articles
        promote_data = []
        promoted_articles = Article.objects.filter(promote=True)
        for promoted_article in promoted_articles:
            promote_data.append({
                'title': promoted_article.title,
                'cover': promoted_article.cover.url,
                'category': promoted_article.category,
                'created_date': promoted_article.created_date,
                'author': promoted_article.author,
                'avatar': promoted_article.author.avatar.url if promoted_article.author.avatar else None,
            })

        context = {
            'article_data': article_data,
            'promote_data': promote_data,
        }

        return render(request, 'index.html', context)


class Contact(TemplateView):
    template_name = "page-contact.html"
