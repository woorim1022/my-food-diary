from datetime import date, timedelta

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

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
    datas = [{
        'name': '회원',
        'data': [10, 100, 500, 20, 100, 5, 15, 20]
    },{
        'name': '비회원',
        'data': [30, 50, 200, 120, 500, 45, 60, 70]
    }];
    context = {
        'datas': datas,
    }
    return JsonResponse(context)

def graph2(request):
    datas = [{
        'name': 'Delivered amount',
        'data': [
            ['Bananas', 50],
            ['Kiwi', 3],
            ['Mixed nuts', 1],
            ['Oranges: 40%', 6],
            ['Apples', 8],
            ['Pears', 4],
            ['Clementines', 4],
            ['Reddish (bag)', 1],
            ['Grapes (bunch)', 1]
        ]
    }]
    context = {
        'datas': datas
    }
    return JsonResponse(context)