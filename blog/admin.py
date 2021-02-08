from django.contrib import admin
from .models import UserProfile, Article, Category


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'article']
    list_display = ['title', 'category', 'author', 'created_date']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover', 'description']


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserprofileAdmin)
