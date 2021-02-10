from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import Article
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        # all articles
        all_article = Article.objects.filter(publish_status='p').order_by('-created_date')
        paginator = Paginator(all_article, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # promoted articles
        promote_data = []
        promoted_articles = Article.objects.filter(promote=True, publish_status='p')
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
            'article_data': page_obj.object_list,
            'promote_data': promote_data,
            'paginator': paginator,
            'page_obj': page_obj
        }

        return render(request, 'index.html', context)


class ContactPage(TemplateView):
    template_name = "page-contact.html"


class AboutPage(TemplateView):
    template_name = "page-about.html"


class AllArticleAPIView(APIView):

    def get(self, request, format=None):
        try:
            all_articles = Article.objects.filter(publish_status='p').order_by('-created_date')[:6]
            data = []
            for article in all_articles:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url,
                    'content': article.content,
                    'author': article.author.name,
                    'created_date': article.created_date,
                    'category': article.category.title,
                    'promote': article.promote,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal Server Error, we\'ll Check it Later'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            article__title = request.GET['article_title']
            article = Article.objects.filter(title__contains=article__title)

            serialized_data = serializers.SingleArticleSerializer(article, many=True)
            data = serialized_data.data

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal Server Error, we\'l Check it Later'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchArticleAPIView(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q

            query = request.GET['query']
            article = Article.objects.filter(Q(content__icontains=query))
            data = []

            for article in article:
                data.append({
                    'title': article.title,
                    'cover': article.cover.url,
                    'content': article.content,
                    'created_date': article.created_date,
                    'author': article.author.name,
                    'category': article.category.title,
                })
                
            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': 'Internal Server Error, we\'l Check it Later'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
