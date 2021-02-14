import math
from ast import literal_eval

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.utils.http import urlencode
from frame.recipeapp.recipeapp_userdb import RecipeDb, IngredientDb, ReviewDb, IngrDb
import frame.mainapp.mainapp_userdb
ingredients = None

def recipe_detail(request):
    # =========================우림 추가코드=====================
    r_id = request.GET['r_id']
    if 'suser' in request.session:
        if request.session['suser']:
            recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])

    # 현재 로그인한 사용자의 최근방문에 추가
    if 'suser' in request.session:
        if request.session['suser']:
             RecipeDb().insert_recent(request.session['suser'], int(r_id))

    # 조회수 증가
    RecipeDb().update_r_view(int(r_id))
    # ==========================우림 추가코드============================

    recipe = RecipeDb().selectall2(int(r_id));
    review = ReviewDb().select(int(r_id));
    # for i in review:
    #     u_id = i.u_id
    #     rv_regdate = i.rv_regdate
    #     r_num = i.r_num
    #     rv_review = i.rv_review
    ingr = IngrDb().select(int(r_id));
    for i in ingr:
        i_name = i.i_name
        ri_q = i.ri_q
        r_regdate = i.r_regdate
        r_view = i.r_view
        r_recommend = i.r_recommend
        r_cooktime = i.r_cooktime
        r_name = i.r_name
        rc_name = i.rc_name
    for i in recipe:
        r_detail = eval(i.r_detail)

    lenth = len(r_detail)+1
    context = {
        'recipe_detail': recipe,
        'review': review,
        'ingr': ingr,
        'r_detail': r_detail,
        'lenth' : lenth,

        # 'u_id' :u_id,
        # 'rv_regdate' : rv_regdate,
        # 'r_num' : r_num,
        # 'rv_review' : rv_review,

        'i_name' : i_name,
        'r_cooktime' : r_cooktime,
        'ri_q' : ri_q,
        'r_regdate' : r_regdate,
        'r_view' : r_view,
        'r_recommend' : r_recommend,
        'rc_name' : rc_name,
        'r_name' : r_name,
        'recent':recent
    }
    return render(request, 'recipeapp/recipe_detail.html', context)
# ==================================송현님코드==========================================================================





# ==================================우림코드=====================================================
def recipe(request):
    #==================================================================
    #==================================================================
    #==================================================================
    # 최근 방문기록 가져와서 뿌려주는 코드
    # 모든 함수에 들어가야됨
    # import frame.mainapp.mainapp_userdb 임포트문에 포함
    # recent 를 context에 넣어주어야 한다
    recent = None
    if 'suser' in request.session:
        if request.session['suser']:
            recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
    #==================================================================
    #==================================================================
    #==================================================================
    ingr_name_user = None
    favorite = None
    rf_qstr = request.GET.get('recipefiltered')
    page = int(request.GET.get('page', '1'))  # 현재 페이지가 있을경우 페이지 값을 가져오고 아닐경우 1로 지정

    # 식재료, 즐겨찾기 출력 코드
    # 세션에 suser 이라는 key가 존재하면
    if 'suser' in request.session:
        # suser이라는 key에 value가 존재하면(즉, 로그인이 되어있으면)
        if request.session['suser']:
            # selectusersingr() 함수를 통해 현재 로그인한 사용자의 식재료"만" 가져온다
            ingr_name_user = IngredientDb().selectusersingr(request.session['suser'])
            ingredients = IngredientDb().selectall()
            # 현재 로그인한 사용자가 즐겨찾기 한 목록 가져오기
            favorite = RecipeDb().select_f_with_u(request.session['suser'])
        # suser이라는 key에 value가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
        else:
            # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
            ingredients = IngredientDb().selectall()
    # 세션에 suser 이라는 key가 존재하지 않으면(즉, 로그인이 되어있지 않으면)
    else:
        # selectall() 함수를 통해 데이터베이스에 있는 모든 식재료를 가져온다
        ingredients = IngredientDb().selectall()

    # 레시피 출력 코드
    # 필터링 선택된 값 없으면(filtering 함수에서 넘어온 값이 없거나 선택한 식재료가 없으면)
    if rf_qstr == None or not rf_qstr:
        # 전체 레시피 select
        recipes = RecipeDb().selectall((page-1)*20);
        recipepage = (RecipeDb().recipepage() + 1);  # 전체페이지수 +1은 초기값이 0이여서 더해둠
    # 필터링 선택된 값 있으면
    else:
        # filtering 함수에서 가져온 id로 recipe를 select
        r_id_list = eval(rf_qstr)
        recipes = RecipeDb().select_with_r_id(r_id_list, (page-1)*20)
        recipepage = len(r_id_list)//20 + 1

    if recipepage // 5 == 0:  # 하단 페이지 링크바 생성을 5개로 지정. 링크바 묶음(1,2,3,4,5),(6,7,8,9,10)
        allpagepart = 1;  # 링크바 묶음 초기값 설정
    else:
        allpagepart = math.ceil(recipepage / 5)  # 전체 링크바 묶음 갯수
    #
    if page // 5 == 0:  # 5개단위묶음 중 현재 몇 묶음에 있는지 확인
        pagepart = 1;  # 현재 묶음 초기값 설정
    else:
        pagepart = math.ceil(page / 5)  # 현재 링크바 묶음 위치

    pagelist = []  # 현재 페이지 기준으로 하단 링크바를 만들기 위한 리스트
    if allpagepart > pagepart:  # 전체 링크바 묶음이 현재 링크바 묶음 위치보다 클 경우
        for l in range(4, -1, -1):
            pagelist.append(pagepart * 5 - l)  # 현재링크바 묶음 위치에 해당하는 5개의 페이지 링크 생성
    elif allpagepart == pagepart:  # 전체 링크바 묶음이 현재 링크바 묶음 위치와 동일하다면
        if recipepage % 5 == 0:  # 총페이지의 개수가 5의배수면 5개 페이지 전체 생성
            for l in range(4, -1, -1):
                pagelist.append(pagepart * 5 - l)
        else:  # 5의배수가 아닐경우
            a = (recipepage % 5)  # 전체페이지를 5로 나눈 나머지값 만큼 페이지 링크 생성
            for l in range(1, a + 1):
                pagelist.append((pagepart - 1) * 5 + l)
    # 다음 버튼을 활성화시키기 위한 조건문
    if allpagepart - pagepart > 0:  # 전체 링크바묶음이 현재 링크바묶음위치보다 클 경우
        next = True
    else:  # 아닐경우
        next = False
    # 이전 버튼을 활성화시키기 위한 조건문
    if pagepart > 1 and allpagepart > 1:  # 전체링크바묶음이 1보다 크면서 현재 링크바묶음이 1보다 클 경우
        before = True
    else:  # 아닐경우
        before = False
    nextnum = (pagepart * 5) + 1  # 다음버튼 누를 경우 하단링크바 묶음 표시
    beforenum = (pagepart - 1) * 5  # 이전버튼 누를 경우 하단링크바 묶음 표시

    context = {
        'recipes': recipes,
        'pagelist': pagelist,
        'pagepart': pagepart,
        'next': next,
        'nextnum': nextnum,
        'before': before,
        'beforenum': beforenum,
        'ingredients': ingredients,
        'ingr_name_user':ingr_name_user,
        'favorite':favorite,
        'recent':recent
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


