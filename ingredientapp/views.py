from datetime import date, timedelta

from django.shortcuts import render, redirect

from frame.ingredientapp.ingredientapp_error import ErrorCode
from frame.ingredientapp.ingredientapp_ingrdb import User_IngrDb, User_AvoidDb, IngrDb


def ingredient(request):
    user_ingrlist = User_IngrDb().select();
    user_avoidlist = User_AvoidDb().select();
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
        if u.ui_exdate - today < greenday and u.ui_exdate - today > redday:
            uigreenlist.append(u)
        elif u.ui_exdate - today < redday:
            uiredlist.append(u)
        else:
            uilist.append(u)

    for ua in user_avoidlist:
        ualist.append(ua)

    context = {
        'ingrlist':ingrlist,
        'uilist':uilist,
        'uiredlist':uiredlist,
        'uigreenlist':uigreenlist,
        'ualist': ualist
    }
    return render(request, 'ingredientapp/ingredient.html',context);


def ingredient_reg(request):
    user_ingrlist = User_IngrDb().select();
    user_avoidlist = User_AvoidDb().select();
    ingr = IngrDb().select();
    ingrlist_icp_name = IngrDb().select_icp_name();
    ingrlist_ic_name = IngrDb().select_ic_name();

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
        if u.ui_exdate - today < greenday and u.ui_exdate - today > redday:
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
        'ualist': ualist,
        'ingr':ingr,
        'ingrlist_icp_name':ingrlist_icp_name,
        'ingrlist_ic_name':ingrlist_ic_name

    }
    return render(request, 'ingredientapp/ingredient_reg.html', context);

def ingredient_regimpl(request):
    i_name = request.POST['i_name']
    i_id = User_IngrDb().select_id(i_name)
    ui_exdate = request.POST['ui_exdate']
    ui_regdate = date.today()
    try:
        User_IngrDb().insert(8,'id01',i_id.i_id,ui_regdate,ui_exdate);
    except:
        context = {
            'error': ErrorCode.e0002
        };
        return render(request,'ingredientapp/ingredient.html',context);
    return redirect('igngredient_reg');
