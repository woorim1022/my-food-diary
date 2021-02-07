import math

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from frame.reviewapp.reviewapp_reviewdb import ReviewDb
from frame.reviewapp.reviewapp_value import Review


def review(request):
    u_id = request.session['suser'] # 로그인된 user아이디 값 가져오기
    page = int(request.GET.get('page','1')) # 현재 페이지가 있을경우 페이지 값을 가져오고 아닐경우 1로 지정

    review = ReviewDb().select(u_id,(page-1)*5); #리뷰데이터 가져와서 객체 생성 offset은 페이지당 5개씩 들어가서 (page-1)*5
    reviewpage = (ReviewDb().reviewpage(u_id)+1); #전체페이지수 +1은 초기값이 0이여서 더해둠

    if reviewpage//5 == 0: # 하단 페이지 링크바 생성을 5개로 지정. 링크바 묶음(1,2,3,4,5),(6,7,8,9,10)
        allpagepart = 1; #링크바 묶음 초기값 설정
    else:
        allpagepart = math.ceil(reviewpage/5) # 전체 링크바 묶음 갯수

    if page//5 == 0: #5개단위묶음 중 현재 몇 묶음에 있는지 확인
        pagepart = 1; # 현재 묶음 초기값 설정
    else:
        pagepart = math.ceil(page/5) # 현재 링크바 묶음 위치

    pagelist = [] #현재 페이지 기준으로 하단 링크바를 만들기 위한 리스트
    if allpagepart > pagepart: # 전체 링크바 묶음이 현재 링크바 묶음 위치보다 클 경우
        for l in range(4,-1,-1):
            pagelist.append(pagepart*5-l) # 현재링크바 묶음 위치에 해당하는 5개의 페이지 링크 생성
    elif allpagepart == pagepart: # 전체 링크바 묶음이 현재 링크바 묶음 위치와 동일하다면
        if reviewpage% 5 == 0: # 총페이지의 개수가 5의배수면 5개 페이지 전체 생성
            for l in range(4, -1, -1):
                pagelist.append(pagepart * 5 - l)
        else: #5의배수가 아닐경우
            a = (reviewpage%5) #전체페이지를 5로 나눈 나머지값 만큼 페이지 링크 생성
            for l in range(1,a+1):
                pagelist.append((pagepart-1)*5+l)

    #다음 버튼을 활성화시키기 위한 조건문
    if allpagepart - pagepart > 0: #전체 링크바묶음이 현재 링크바묶음위치보다 클 경우
        next = True
    else: #아닐경우
        next = False

    #이전 버튼을 활성화시키기 위한 조건문
    if pagepart >1 and allpagepart>1: #전체링크바묶음이 1보다 크면서 현재 링크바묶음이 1보다 클 경우
        before = True
    else: #아닐경우
        before = False
    nextnum = (pagepart*5)+1 #다음버튼 누를 경우 하단링크바 묶음 표시
    beforenum = (pagepart-1)*5 #이전버튼 누를 경우 하단링크바 묶음 표시
    context = {
        'review':review,
        'pagelist':pagelist,
        'reviewpage':reviewpage,
        'pagepart':pagepart,
        'next':next,
        'nextnum':nextnum,
        'before':before,
        'beforenum':beforenum
    }
    return render(request,'reviewapp/review.html',context)