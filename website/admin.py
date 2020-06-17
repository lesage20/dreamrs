from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'phone', 'addresse', 'email', ]
    search_field = ['name', 'email', 'phone']
    ordering = ['date_add','name']
    
    

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['geolocation', 'name', 'subject', 'email' ]

@admin.register(models.NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_per_page = 10
    ordering = ['date_add']
    date_hierarchy = 'date_add'

@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'first_name', 'job', 'icon', 'message']
    search_field = ['name', 'message']
    ordering = ['date_add', 'name']


@admin.register(models.SocialAccounts)
class SocialAccounts(admin.ModelAdmin):
    list_display = ['name', 'icon', 'link' ]
    search_field = ['name']



