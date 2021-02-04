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
from django.views.generic import TemplateView

from userapp import views

urlpatterns = [
    path('mypage', TemplateView.as_view(template_name='userapp/mypage.html'), name='mypage'),
    path('profile', views.UserView.profile, name='profile'),
    path('userupdateimple', views.UserView.userupdateimple,name='userupdateimple'),

    path('ncheck',views.UserView.ncheck,name='ncheck'),

    path('myrecipereg',TemplateView.as_view(template_name='myrecipereg.html'),name='myrecipereg'),
    path('ingredient', TemplateView.as_view(template_name='ingredientapp/ingredient.html'),name='ingredient'),
    path('like',TemplateView.as_view(template_name='like.html'),name='like'),
    path('review',TemplateView.as_view(template_name='review.html'),name='review'),
    path('allergy',TemplateView.as_view(template_name='allergy.html'),name='allergy'),
]
