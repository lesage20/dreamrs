from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'first_name', 'icon']
    search_field = ['name',]
    ordering = ['name', ]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_article']
    search_field = ['name']
    ordering = ['name', 'number_article']

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'category', 'author']
    search_field = ['title', 'category', 'author']
    ordering = ['title' ]

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['commentator_name', 'commentator_first_name', 'icon']
    search_field = ['commentator_name', 'commentator_first_name']
    ordering = ['commentator_name', ]

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['name', 'like_status', 'article']
    search_field = ['name', 'article']
    ordering = ['name', ]