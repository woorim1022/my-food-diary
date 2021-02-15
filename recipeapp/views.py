import math
from ast import literal_eval

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.utils.http import urlencode
from frame.recipeapp.recipeapp_userdb import RecipeDb, IngredientDb, ReviewDb, IngrDb
import frame.mainapp.mainapp_userdb
ingredients = None
rid_global = None
iid_global = None


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

    for i in recipe:
        r_detail = eval(i.r_detail)

    context = {
        'recipe_detail': recipe,
        'review': review,
        'ingr': ingr,
        'r_detail': r_detail,
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

    global rid_global
    global iid_global

    ingr_checked = None
    favorite = None

    # filtering 함수로부터 오는 요청
    r_qstr = request.GET.get('r_id_list')
    i_qstr = request.GET.get('i_id_list')

    # recipe.html로부터 호는 요청
    page_r = int(request.GET.get('page_r', '1'))  # 현재 페이지가 있을경우 페이지 값을 가져오고 아닐경우 1로 지정
    # page_i = int(request.GET.get('page_i', '1'))
    filtered = request.GET.get('filtered','False')

    print('@@@@@@@@@@@@@@'+filtered)

    # 식재료 출력 코드
    # ingr = IngredientDb().selectall((page_i - 1) * 30)
    # ingr_page = (IngredientDb().ingrpage() + 1);
    ingr = IngredientDb().selectall()
    # 체크박스에 체크할 식재료 가져오는 코드
    # filtering 함수에서 쿼리스트링을 가져왔거나 filtered가 True이면 즉, 필터링 된 상태면
    if (i_qstr != None and i_qstr != '[]') or filtered == 'True':
        # recipe.html에서 페이지 버튼을 누른 경우
        if filtered == 'True':
            # 전역변수에 저장해놓은 iid 리스트를 가져옴
            i_id_list = iid_global
        else:
            i_id_list = eval(i_qstr)
        iid_global = i_id_list
        ingr_checked = IngredientDb().select_checked_ingr(i_id_list)
    # 식재료 쿼리스트링이 비어있고 필터링 된 상태도 아니면
    else:
        # 로그인 되어있으면
        if 'suser' in request.session:
            if request.session['suser']:
                u_id = request.session['suser']
                ingr_checked = IngredientDb().selectusersingr(u_id)

    # 레시피 출력 코드
    if (r_qstr != None and r_qstr != '[]') or filtered == 'True':
        if filtered == 'True':
            r_id_list = rid_global
        else:
            r_id_list = eval(r_qstr)
        recipes = RecipeDb().select_with_r_id(r_id_list, (page_r - 1) * 20)
        recipepage = len(r_id_list) // 20 + 1
        rid_global = r_id_list
        filtered = 'True'
    else:
        recipes = RecipeDb().selectall((page_r - 1) * 20);
        recipepage = (RecipeDb().recipepage() + 1);

    # 즐겨찾기 출력 코드
    if 'suser' in request.session:
        if request.session['suser']:
            u_id = request.session['suser']
            favorite = RecipeDb().select_f_with_u(u_id)


    if recipepage // 5 == 0:  # 하단 페이지 링크바 생성을 5개로 지정. 링크바 묶음(1,2,3,4,5),(6,7,8,9,10)
        allpagepart = 1;  # 링크바 묶음 초기값 설정
    else:
        allpagepart = math.ceil(recipepage / 5)  # 전체 링크바 묶음 갯수
    if page_r // 5 == 0:  # 5개단위묶음 중 현재 몇 묶음에 있는지 확인
        pagepart = 1;  # 현재 묶음 초기값 설정
    else:
        pagepart = math.ceil(page_r / 5)  # 현재 링크바 묶음 위치

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
        'ingredients': ingr,
        'ingr_checked':ingr_checked,
        'favorite':favorite,
        'recent':recent,
        'filtered':filtered
    }
    return render(request, 'recipeapp/recipe.html', context);


def filtering(request):
    r_id_list = []
    i_id_list = request.POST.getlist('ingrcheck[]')
    for i in range(len(i_id_list)):
        i_id_list[i] = int(i_id_list[i])

    for i in i_id_list:
        # i를 포함한 레시피 select로 가져와
        recipewithingr = RecipeDb().select_recipe_with_ingr(i)

        # r_id 리스트에 저장하는 부분
        for j in range(len(recipewithingr)):
           # 겹치면 저장 ㄴㄴ
           if recipewithingr[j].r_id in r_id_list:
               continue
           else:
               r_id_list.append(recipewithingr[j].r_id)

    qstr_r = urlencode({'r_id_list':r_id_list})
    qstr_i = urlencode({'i_id_list':i_id_list})
    return HttpResponseRedirect('%s?%s&%s' % ('recipe', qstr_r, qstr_i))


def fav_add(request):
    # 로그인 안했으면 아무것도 안함
    # 로그인 했으면 favorite 테이블에 insert
    r_id = request.GET['r_id']
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
    # 로그인 안했으면 아무것도 안함
    # 로그인 했으면 favorite 테이블에서 delete
    r_id = request.GET['r_id']
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


