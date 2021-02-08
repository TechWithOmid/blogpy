from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='files/images/avatar/', blank=True)
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.ImageField(upload_to='files/images/article_cover/')
    article = RichTextField()
    created_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    cover = models.ImageField(upload_to='files/images/category_cover')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.title
