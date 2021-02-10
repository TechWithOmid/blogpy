from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name="home"),
    url(r'^contact/$', views.ContactPage.as_view(), name="contact"),
    url(r'^about/$', views.AboutPage.as_view(), name="about"),

    url(r'^article/$', views.SingleArticleAPIView.as_view(), name="single_article"),
    url(r'^article/search/$', views.SearchArticleAPIView.as_view(), name="search_article"),
    url(r'^article/submit/$', views.SubmitArticleAPIView.as_view(), name="submit_article"),
    url(r'^article/update-cover/$', views.UpdateArticleCoverAPIView.as_view(), name="update_article_cover"),
    url(r'^article/all/$', views.AllArticleAPIView.as_view(), name="all_articles"),
    url(r'^article/delete/$', views.DeleteArticleAPIView.as_view(), name="delete_article"),
]
