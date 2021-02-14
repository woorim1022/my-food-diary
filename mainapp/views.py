from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.http import urlencode

from frame.mainapp.mainapp_userdb import UserDb, RecipeDb, ReviewDb
import frame.myrecipeapp.myrecipeapp_userdb

def main(request):
    allrecipes = RecipeDb().select()
    reviews = ReviewDb().select_review()
    # 오늘의 추천 구현하기
    todayrecommend = RecipeDb().select_toprecommend()

    recent = None
    if 'suser' in request.session:
        if request.session['suser']:
            recent = RecipeDb().select_recent(request.session['suser'])
    context = {
        'allrecipes': allrecipes,
        'recent':recent,
        'reviews':reviews,
        'todayrecommend':todayrecommend
    };
    return render(request, 'mainapp/main.html', context)

# 회원가입 페이지로 넘어가는 함수
def userreg(request):
    return render(request,'mainapp/userreg.html')

# 회원가입 처리하는 함수
def useraddimpl(request):
    u_id = request.POST['u_id']
    u_nick = request.POST['u_nick']
    u_pwd_1 = request.POST['u_pwd_1']
    u_pwd_2 = request.POST['u_pwd_2']
    u_name = request.POST['u_name']
    u_age = request.POST['u_age']
    allrecipes = RecipeDb().select()
    reviews = ReviewDb().select_review()
    recent = None
    todayrecommend = RecipeDb().select_toprecommend()

    if 'suser' in request.session:
        if request.session['suser']:
            recent = RecipeDb().select_recent(request.session['suser'])

    if u_pwd_1 != u_pwd_2:
        context = {
            'message': '회원가입 실패'
        };
        return render(request, 'mainapp/userreg.html', context);
    else:
        try:
            UserDb().insert(u_id,u_nick,u_pwd_1,u_name,int(u_age));
        except:
            context = {
                'message': '회원가입 실패'
            };
            return render(request,'mainapp/userreg.html',context);
        context = {
            'login': 'success',
            'message': '회원가입 완료',
            'nickname' : u_nick,
            'allrecipes': allrecipes,
            'reviews':reviews,
            'recent':recent,
            'todayrecommend':todayrecommend
        };
        request.session['suser'] = u_id
        request.session['snickname'] = u_nick
        return render(request, 'mainapp/main.html', context)


def idcheck(request):
    id = request.GET['id']
    if id == '':
        return HttpResponse('empty')
    try:
        UserDb().selectid(id)
    # 중복이 아니면
    except:
        return HttpResponse('ok')
    return HttpResponse('no')


def nickcheck(request):
    nickname = request.GET['nickname']
    if nickname == '':
        return HttpResponse('empty')
    try:
        UserDb().selectnick(nickname)
    # 중복이 아니면
    except:
        return HttpResponse('ok')
    return HttpResponse('no')



def login(request):
    return render(request, 'mainapp/login.html')



# 로그인 처리하는 함수
def loginimpl(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    allrecipes = RecipeDb().select()
    reviews = ReviewDb().select_review()
    recent = None
    todayrecommend = RecipeDb().select_toprecommend()

    try:
        user = UserDb().selectid(id);
        # 비밀번호가 일치하는 경우, 로그인 성공한 경우
        if pwd == user.u_pwd:
            request.session['suser'] = id
            request.session['snickname'] = user.u_nick
            if 'suser' in request.session:
                if request.session['suser']:
                    recent = RecipeDb().select_recent(request.session['suser'])
            context = {
                'login':'success',
                'message': '로그인 완료',
                'nickname': user.u_nick,
                'allrecipes': allrecipes,
                'reviews': reviews,
                'recent': recent,
                'todayrecommend':todayrecommend
            };
        else:
            raise Exception
    # 로그인 실패인 경우
    except:
        context = {
            'login':'fail',
            'message': '로그인 실패',
            'allrecipes':allrecipes,
            'reviews': reviews,
            'recent': recent,
            'todayrecommend': todayrecommend
        };
        return render(request, 'mainapp/main.html', context)
    return render(request, 'mainapp/main.html', context)


def logout(request):
    if 'suser' in request.session:
        if request.session['suser']:
            del request.session['suser']
    if 'snickname' in request.session:
        if request.session['snickname']:
            del request.session['snickname']
    return redirect('main')