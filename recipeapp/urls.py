"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipeapp import views

urlpatterns = [
    path('recipe', views.recipe, name='recipe'),
    path('recipe_detail', views.recipe_detail, name='recipe_detail'),
    path('filtering', views.filtering, name='filtering'),

    #댓글 연결
    path('review_impl', views.review_impl, name='review_impl'),

    path('fav_add/', views.fav_add, name='fav_add'),
    path('fav_cancel/', views.fav_cancel, name='fav_cancel'),

    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
]
