from datetime import date, timedelta

from django.shortcuts import render

from frame.ingredientapp.ingredientapp_ingrdb import User_IngrDb, User_AvoidDb, IngrDb


def ingredient(request):
    user_ingrlist = User_IngrDb().select();
    user_avoidlist = User_AvoidDb().select();
    today = date.today()
    greenday = timedelta(days=5)
    redday = timedelta(days=0)
    uiredlist = [];
    uigreenlist = [];
    uaredlist = [];
    uagreenlist = [];
    ualist = [];
    for u in user_ingrlist:
        if u.ui_exdate - today < greenday and u.ui_exdate - today > redday:
            uigreenlist.append(u)
        elif u.ui_exdate - today < redday:
            uiredlist.append(u)

    for ua in user_avoidlist:
        if ua.ui_exdate - today < greenday and ua.ui_exdate - today > redday:
            uagreenlist.append(ua)
        elif ua.ui_exdate - today < redday:
            uaredlist.append(ua)
        else:
            ualist.append(ua)


    context = {
        'user_ingrlist':user_ingrlist,
        'today': today,
        'uiredlist':uiredlist,
        'uigreenlist':uigreenlist,
        'uaredlist': uaredlist,
        'uagreenlist': uagreenlist,
        'ualist': ualist
    }
    return render(request, 'ingredientapp/ingredient.html',context);


def ingredient_reg(request):
    user_ingrlist = User_IngrDb().select();
    ingrlist = IngrDb().select();
    today = date.today()

    context = {
        'user_ingrlist': user_ingrlist,
        'ingrlist': ingrlist,
        'today': today,
    }
    return render(request, 'ingredientapp/ingredient_reg.html', context);
