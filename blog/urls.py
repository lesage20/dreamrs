from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('details', views.details, name='details'),
]
