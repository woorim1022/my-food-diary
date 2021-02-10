from django.shortcuts import render
import frame.mainapp.mainapp_userdb

# Create your views here.
def myrecipe(request):
    # ==================================================================
    # ==================================================================
    # ==================================================================
    # 최근 방문기록 가져와서 뿌려주는 코드
    # 모든 함수에 들어가야됨
    # import frame.mainapp.mainapp_userdb 임포트문에 포함
    # recent 를 context에 넣어주어야 한다
    if 'suser' in request.session:
        if request.session['suser']:
            recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
    # ==================================================================
    # ==================================================================
    # ==================================================================
    context = {
        'recent': recent
    }


    return render(request, 'myrecipeapp/myrecipe.html', context)