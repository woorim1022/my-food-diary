import datetime
from datetime import date, timedelta

from django.shortcuts import render, redirect

from frame.ingredientapp.ingredientapp_error import ErrorCode
from frame.ingredientapp.ingredientapp_ingrdb import User_IngrDb, User_AvoidDb, IngrDb



def ingredient(request):
    if  'suser' in request.session:
        u_id = request.session['suser']
        user_ingrlist = User_IngrDb().select(u_id);
        user_avoidlist = User_AvoidDb().select(u_id);
        today = date.today()
        greenday = timedelta(days=5)
        redday = timedelta(days=0)
        uiredlist = [];
        uigreenlist = [];
        uilist = [];
        ualist = [];
        ingrlist = [];

        for u in user_ingrlist:
            ingrlist.append(u)
        for u in user_ingrlist:
            if u.ui_exdate - today < greenday and u.ui_exdate - today >= redday:
                uigreenlist.append(u)
            elif u.ui_exdate - today < redday:
                uiredlist.append(u)
            else:
                uilist.append(u)

        for ua in user_avoidlist:
            ualist.append(ua)

        context = {
            'ingrlist': ingrlist,
            'uilist': uilist,
            'uiredlist': uiredlist,
            'uigreenlist': uigreenlist,
            'ualist': ualist
        }
        return render(request, 'ingredientapp/ingredient.html', context);
    else:
        context = {
            'error':ErrorCode.e0003
        }
    return render(request,'ingredientapp/ingredient.html',context);


def ingredient_reg(request):
    u_id = request.session['suser']
    user_ingrlist = User_IngrDb().select(u_id);
    user_avoidlist = User_AvoidDb().select(u_id);
    ingrlist_i_name = IngrDb().select_i_name();
    today = date.today()
    greenday = timedelta(days=5)
    redday = timedelta(days=0)
    uiredlist = [];
    uigreenlist = [];
    uilist = [];
    ualist = [];
    ingrlist = [];
    for u in user_ingrlist:
        ingrlist.append(u)
    for u in user_ingrlist:
        if u.ui_exdate - today < greenday and u.ui_exdate - today >= redday:
            uigreenlist.append(u)
        elif u.ui_exdate - today < redday:
            uiredlist.append(u)
        else:
            uilist.append(u)

    for ua in user_avoidlist:
        ualist.append(ua)

    context = {
        'ingrlist': ingrlist, #전체리스트
        #전체날짜리스트
        'uilist': uilist, #5일 이상 리스트
        'uiredlist': uiredlist, #유통기한 지난 리스트
        'uigreenlist': uigreenlist, #5일 이내 리스트
        'ualist': ualist, #알레르기 유발 리스트
        'ingrlist_i_name':ingrlist_i_name #식재료 이름 중복 제거

    }
    return render(request,'ingredientapp/ingredient_reg.html', context);

def ingredient_regimpl(request):
    u_id = request.session['suser']
    i_name = request.POST['i_name']
    i_id = IngrDb().select_id(i_name) #식재료 이름으로 식재료 아이디값 찾기 클래스 형태이므로 i_id.i_id로 불러내야함
    ui_exdate = request.POST['ui_exdate']
    ui_regdate = date.today()
    try:
        User_IngrDb().insert(u_id,i_id.i_id,ui_regdate,ui_exdate);
    except:
        context = {
            'error' : ErrorCode.e0002
        }
        return redirect('ingredient');
    return redirect('ingredient_reg');

def ingredient_regdel(request):
    u_id = request.session['suser']
    i_name = request.POST['i_name']
    i_id = IngrDb().select_id(i_name) #식재료 이름으로 식재료 아이디값 찾기 클래스 형태이므로 i_id.i_id로 불러내야함
    ui_exdate = request.POST['ui_exdate']
    ui_exdate = datetime.datetime.strptime(ui_exdate,'%b. %d, %Y')
    try:
        User_IngrDb().delete(i_id.i_id,u_id,ui_exdate);
    except:
        context = {
            'error': ErrorCode.e0002
        }
        return redirect('ingredient_reg');
    return redirect('ingredient_reg');

def ingredient_update(request):
    i_name = request.POST['i_name']
    ui_exdate = request.POST['ui_exdate']
    ui_id = request.POST['u_id']
    i_id = IngrDb().select_id(i_name)  # 식재료 이름으로 식재료 아이디값 찾기 클래스 형태이므로 i_id.i_id로 불러내야함
    ui_exdate = datetime.datetime.strptime(ui_exdate, '%Y-%m-%d')
    try:
        User_IngrDb().update(i_id.i_id,int(ui_id),ui_exdate);
    except:
        context = {
            'error': ErrorCode.e0002
        }
        return redirect('ingredient_reg');
    return redirect('ingredient_reg');