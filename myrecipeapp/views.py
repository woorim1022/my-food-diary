import math

from django.shortcuts import render
from frame.myrecipeapp.myrecipeapp_userdb import RecipeDb
import frame.mainapp.mainapp_userdb
# Create your views here.
def myrecipe(request):
    page = int(request.GET.get('page', '1'))
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
    message = None
    recipes = None
    recipepage = 0
    maxregdate = None
    maxrecommend = None
    maxview = None
    if 'suser' in request.session:
        if request.session['suser']:
            # 전체
            recipes = RecipeDb().selectall(request.session['suser'], (page-1)*12)
            recipepage = (RecipeDb().recipepage(request.session['suser'])+1)
            # 최근등록
            maxregdate = RecipeDb().select_maxregdate(request.session['suser'])[0]
            # 최다 추천
            maxrecommend = RecipeDb().select_maxrecommend(request.session['suser'])[0]
            # 최다 조회
            maxview = RecipeDb().select_maxview(request.session['suser'])[0]

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
                'recent': recent,
                'recipes': recipes,
                'maxregdate': maxregdate,
                'maxrecommend': maxrecommend,
                'maxview': maxview,
                'pagelist': pagelist,
                'pagepart': pagepart,
                'next': next,
                'nextnum': nextnum,
                'before': before,
                'beforenum': beforenum
            }

        else:
            message = '로그인 해주세요'
            context = {
                'message': message
            }
    else:
        message = '로그인 해주세요'
        context = {
            'message': message
        }
    return render(request, 'myrecipeapp/myrecipe.html', context)