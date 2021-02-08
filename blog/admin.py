from django.contrib import admin
from .models import UserProfile, Article, Category


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'article']
    ordering = ['-created_date']
    list_filter = ('category', 'created_date', 'author')
    list_display = ['promote',  'created_date', 'category', 'author', 'title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover', 'description']


class UserprofileAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile, UserprofileAdmin)
