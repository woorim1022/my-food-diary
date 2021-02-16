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

    path('mypage', views.UserView.mypage, name='mypage'),
    path('profile', views.UserView.profile, name='profile'),
    path('userupdateimple', views.UserView.userupdateimple,name='userupdateimple'),
    path('ncheck/',views.UserView.ncheck,name='ncheck'),

    path('myrecipe_reg',views.UserView.myrecipereg,name='myrecipe_reg'),
    path('myrecipeaddimpl', views.UserView.myrecipeaddimpl,name='myrecipeaddimpl'),
    path('recipeingrcheck',TemplateView.as_view(template_name='userapp/recipeingrcheck.html'),name='recipeingrcheck'),
    path('recipeingradd',views.UserView.recipeingradd,name='recipeingradd'),

    path('popingr.html',views.UserView.popingr, name='popingr'),
    path('popsearch/',views.UserView.popsearch,name='popsearch'),

    path('like',TemplateView.as_view(template_name='like.html'),name='like'),

    path('allergy',views.UserView.allergy,name='allergy'),
    path('allergyrem',views.UserView.allergyrem,name='allergyrem'),
    path('allergyadd',views.UserView.allergyadd,name='allergyadd')
]
