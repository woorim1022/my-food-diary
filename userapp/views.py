from django.http import HttpResponse
from django.shortcuts import render, redirect

from frame.userapp.userapp_userdb import UserDb


class UserView:
    def profile(request):
        return render(request,'userapp/profile.html')

    def userupdateimple(request):
        u_id = request.POST['id'];
        u_nick = request.POST['nick'];
        u_pwd = request.POST['reusepwd'];
        u_name = request.POST['name'];
        u_age = request.POST['age'];
        try:
            UserDb().update(u_id, u_nick, u_pwd, u_name, int(u_age))
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

