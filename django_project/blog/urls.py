from django.urls import path
from . import views

urlpatterns = [
    # empty path as home page, puttin
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
