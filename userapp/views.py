from django.http import HttpResponse
from django.shortcuts import render, redirect

from frame.userapp.userapp_userdb import UserDb


class UserView:
    def profile(request):
        return render(request,'userapp/profile.html')

    def userupdateimple(request):
        id = request.POST['id'];
        nick = request.POST['nick'];
        pwd = request.POST['reusepwd'];
        name = request.POST['name'];
        age = request.POST['age'];
        try:
            UserDb().update(id, nick, pwd, name, int(age))
        except:
            return render(request,'userapp/profile.html');
        return render(request,'userapp/mypage.html')

    def ncheck(request):
        nick = request.GET['nck'];
        nicklist = UserDb().ncheck();
        if nick == '':
            return HttpResponse('0');
        try:
            if nick not in nicklist:
                return HttpResponse('2');
        except:
            return HttpResponse('1')

