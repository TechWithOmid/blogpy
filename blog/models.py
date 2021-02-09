from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to='files/images/avatar/', blank=True)
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='عنوان')
    cover = models.ImageField(upload_to='files/images/article_cover/')
    content = RichTextField()
    created_date = models.DateTimeField(default=datetime.now, verbose_name='تاریخ')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='دسته')
    promote = models.BooleanField(default=False, editable=True, verbose_name='اسلایدر')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


class Category(models.Model):
    cover = models.ImageField(upload_to='files/images/category_cover')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = ' دسته بندی ها'

    def __str__(self):
        return self.title
