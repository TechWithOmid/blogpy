from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name="home"),
    url(r'^contact$', views.Contact.as_view(), name="contact")
]
