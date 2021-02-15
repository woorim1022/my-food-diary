from datetime import date, timedelta

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from frame.adminapp.adminapp_userdb import UsersDb


def adminpage(request):
    today = date.today()
    day = timedelta(days=8)
    startday = today - day
    context = {
        'today': today,
        'startday': startday
    }
    return render(request, 'adminapp/adminpage.html',context);

def graph1(request):
    today = date.today()
    day = timedelta(days=8)
    startday = today - day
    datas = [{
        'name': '회원',
        'data': [10, 100, 500, 20, 100, 5, 15, 20]
    },{
        'name': '비회원',
        'data': [30, 50, 200, 120, 500, 45, 60, 70]
    }];
    context = {
        'datas': datas,
        'today': today,
        'day': day,
        'startday': startday
    }
    return JsonResponse(context)

def graph2(request):
    teen = UsersDb().select(10,20)
    twenty = UsersDb().select(20,30)
    thirty = UsersDb().select(30,40)
    forty = UsersDb().select(40,50)
    fifty = UsersDb().select(50,60)
    sixty = UsersDb().select(60,70)
    old = UsersDb().select(70,150)
    sumage = teen + twenty + thirty + forty + fifty + sixty +old

    datas = [{
        'name': '회원수',
        'data': [
            ['10대 '+str(teen/sumage*100)+'%', teen],
            ['20대 '+str(twenty/sumage*100)+'%', twenty],
            ['30대 '+str(thirty/sumage*100)+'%', thirty],
            ['40대 '+str(forty/sumage*100)+'%', forty],
            ['50대 '+str(fifty/sumage*100)+'%', fifty],
            ['60대 '+str(sixty/sumage*100)+'%', sixty],
            ['60대이상 '+str(old/sumage*100)+'%', old],
        ]
    }]
    context = {
        'datas': datas
    }
    return JsonResponse(context)
def graph3(request):
    recipe = UsersDb().recipe_select();
    datas = []
    for r in recipe:
        datas.append([r.r_name,r.r_view])

    context = {
        'datas': datas
    }
    return JsonResponse(context)

def graph4(request):
    datas = [
            ['김치', 300],
            ['삼겹살', 150],
            ['케찹', 130],
            ['설탕', 110],
            ['닭봉', 90],
            ['안심', 80],
            ['명란젓', 80],
            ['스팸', 50],
            ['라면', 40],
            ['참치', 20],
        ]
    context = {
        'datas': datas
    }
    return JsonResponse(context)
