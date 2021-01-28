from django.shortcuts import render, redirect

# Create your views here.
from frame.userdb import UserDb


def userreg(request):
    context = {
        'section':'userreg'
    }
    return render(request,'myfooddiary/main.html',context)

def useraddimpl(request):
    u_id = request.POST['u_id']
    u_nick = request.POST['u_nick']
    u_pwd = request.POST['u_pwd']
    u_name = request.POST['u_name']
    u_age = request.POST['u_age']
    try:
        UserDb().insert(u_id,u_nick,u_pwd,u_name,int(u_age));
    except:
        context = {
            'section':'userreg',
            'message': '아이디가 중복 되었거나 나이값이 숫자가 아닙니다'
        };
        return render(request,'myfooddiary/main.html',context);
    context = {
        'message': '회원가입 완료',
        'u_nick' : u_nick
    };
    return render(request,'myfooddiary/main.html',context);

