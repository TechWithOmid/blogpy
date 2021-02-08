from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import Article


class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        # all articles
        article_data = []
        all_article = Article.objects.all().order_by('-created_date')
        paginator = Paginator(all_article, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

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
            'article_data': page_obj.object_list,
            'promote_data': promote_data,
            'paginator': paginator,
            'page_obj': page_obj
        }

        return render(request, 'index.html', context)


class Contact(TemplateView):
    template_name = "page-contact.html"
