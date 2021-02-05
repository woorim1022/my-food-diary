from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.utils.http import urlencode
from frame.recipeapp.recipeapp_userdb import RecipeDb, IngredientDb, ReviewDb
ingredients = None



# ==================================송현님코드================================================================

def recipe_detail(request):
    recipe = RecipeDb().select();
    review = ReviewDb().select();
    context = {
        'recipe_detail': recipe,
        'review': review
    }
    return render(request, 'recipeapp/recipe_detail.html', context)
# ==================================송현님코드==========================================================================












# ==================================우림코드=====================================================

def recipe(request):
    global ingredients
    recipefiltered = request.GET.get('recipefiltered')
    print(type(recipefiltered))
    # eval사용하기
    # 세션에 suser 이라는 key가 존재하면
    if 'suser' in request.session:
        # suser이라는 key에 value가 존재하면(즉, 로그인이 되어있으면)
        if request.session['suser']:
            # selectusersingr() 함수를 통해 현재 로그인한 사용자의 식재료"만" 가져온다
            ingredients = IngredientDb().selectusersingr(request.session['suser'])
        # suser이라는 key에 value가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
        else:
            # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
            ingredients = IngredientDb().selectall()
    # 세션에 suser 이라는 key가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
    else:
        # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
        ingredients = IngredientDb().selectall()

    if recipefiltered == None or not recipefiltered:
        recipes = RecipeDb().selectall();
    else:
        temp = [];
        for i in range(len(recipefiltered)):
            print(recipefiltered[i])
            # if recipefiltered[i] != '[' or recipefiltered[i] != ']' or recipefiltered[i] != ',' or recipefiltered[i] != ' ':
            #     temp.append(RecipeDb().select_with_r_id(int(recipefiltered[i])))
        recipes = temp;
    context = {
        'recipes': recipes,
        'ingredients': ingredients
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
    print(recipefiltered)
    qstr = urlencode({'recipefiltered':recipefiltered})
    return HttpResponseRedirect('%s?%s' % ('recipe', qstr))

# ===============================================우림코드==============================================================


