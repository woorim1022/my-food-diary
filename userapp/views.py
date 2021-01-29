from django.shortcuts import render, redirect


def mypage(request):
    return render(request, 'userapp/mypage.html');


def profile(request):
    return render(request, 'userapp/profile.html');