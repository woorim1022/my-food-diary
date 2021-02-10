from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.utils.http import urlencode
from frame.recipeapp.recipeapp_userdb import RecipeDb, IngredientDb, ReviewDb, IngrDb
import frame.mainapp.mainapp_userdb
ingredients = None

# def recent():
#     if 'suser' in request.session:
#         if request.session['suser']:
#             recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
#     return recent
# ==================================송현님코드================================================================

def recipe_detail(request):
    # =========================우림 추가코드=====================
    r_id = request.GET['r_id']
    # 현재 로그인한 사용자의 최근방문에 추가
    if 'suser' in request.session:
        if request.session['suser']:
             RecipeDb().insert_recent(request.session['suser'], int(r_id))

    # 조회수 증가
    RecipeDb().update_r_view(int(r_id))
    # ==========================우림 추가코드============================

    recipe = RecipeDb().selectall2(1);
    review = ReviewDb().select(1);
    ingr = IngrDb().select(1);
    for i in recipe:
        r_detail = eval(i.r_detail)
        r_dimage = eval(i.r_dimage)
    context = {
        'recipe_detail': recipe,
        'review': review,
        'ingr': ingr,
        'r_dimage': r_dimage,
        'r_detail': r_detail
    }
    return render(request, 'recipeapp/recipe_detail.html', context)
# ==================================송현님코드==========================================================================





# ==================================우림코드=====================================================

def recipe(request):
    global ingredients
    ingr_name_user = None
    favorite = None
    recipefiltered_str = request.GET.get('recipefiltered')
    if recipefiltered_str != None:
        recipefiltered = eval(recipefiltered_str)
    # eval사용하기

    # 식재료 출력 코드
    # 세션에 suser 이라는 key가 존재하면
    if 'suser' in request.session:
        # suser이라는 key에 value가 존재하면(즉, 로그인이 되어있으면)
        if request.session['suser']:
            # selectusersingr() 함수를 통해 현재 로그인한 사용자의 식재료"만" 가져온다
            ingr_name_user = IngredientDb().selectusersingr(request.session['suser'])
            ingredients = IngredientDb().selectall()
            favorite = RecipeDb().select_f_with_u(request.session['suser'])

            # 최근 방문 추가
           # recent = recent();




        # suser이라는 key에 value가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
        else:
            # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
            ingredients = IngredientDb().selectall()

    # 세션에 suser 이라는 key가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
    else:
        # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
        ingredients = IngredientDb().selectall()


    # 레시피 출력 코드
    # 필터링 선택된 값 없으면
    if recipefiltered_str == None or not recipefiltered_str:
        # 전체 레시피 출력
        recipes = RecipeDb().selectall();
    # 필터링 선택된 값 있으면
    else:
        # filtering 함수에서 가져온 id로 recipe를 select
        temp = [];
        for i in range(len(recipefiltered)):
            # print(recipefiltered[i])
            temp.append(RecipeDb().select_with_r_id(recipefiltered[i])[0])
        recipes = temp;


    context = {
        'recipes': recipes,
        'ingredients': ingredients,
        'ingr_name_user':ingr_name_user,
        'favorite':favorite
    }
    return render(request, 'recipeapp/recipe.html', context);


def filtering(request):
    recipefiltered = []
    ingrchecklist = request.POST.getlist('ingrcheck[]')
    for i in ingrchecklist:
        # i를 포함한 레시피 select로 가져와
        recipewithingr = RecipeDb().select_recipe_with_ingr(int(i))
        for j in range(len(recipewithingr)):
           # 겹치면 저장 ㄴㄴ
           if recipewithingr[j].r_id in recipefiltered:
               continue
           else:
               recipefiltered.append(recipewithingr[j].r_id)
    # print(recipefiltered)
    qstr = urlencode({'recipefiltered':recipefiltered})
    return HttpResponseRedirect('%s?%s' % ('recipe', qstr))


def fav_add(request):
    print('fav_add')
    # 로그인 안했으면 아무것도 안함
    # 로그인 했으면 favorite 테이블에 insert
    r_id = request.GET['r_id']
    print(r_id)
    u_id = None
    if 'suser' in request.session:
        # suser이라는 key에 value가 존재하면(즉, 로그인이 되어있으면)
        if request.session['suser']:
            u_id = request.session['suser']
            RecipeDb().insert_fav(u_id, int(r_id))
            return HttpResponse('ok')
        else:
            return HttpResponse('no')
    else:
        return HttpResponse('no')


def fav_cancel(request):
    print('fav_cancel')
    # 로그인 안했으면 아무것도 안함
    # 로그인 했으면 favorite 테이블에서 delete
    r_id = request.GET['r_id']
    print(r_id)
    u_id = None
    if 'suser' in request.session:
        # suser이라는 key에 value가 존재하면(즉, 로그인이 되어있으면)
        if request.session['suser']:
            u_id = request.session['suser']
            RecipeDb().insert_fav(u_id, int(r_id))
            return HttpResponse('ok')
        else:
            return HttpResponse('no')
    else:
        return HttpResponse('no')

# ===============================================우림코드==============================================================


