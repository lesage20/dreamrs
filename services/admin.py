from django.contrib import admin

# Register your models here.
from .import models

@admin.register(models.Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['type_apartment', ]
    search_field = ['type_apartement']


@admin.register(models.Service)
class ServicetAdmin(admin.ModelAdmin):
    list_display = ['nom', 'image']
    search_field = ['nom']
    ordering = ['nom', 'date_add']


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['domaine','titre', 'nouveau_projet']
    search_display = ['domaine', 'nouveau_projet']
    ordering = ['domaine', 'titre']