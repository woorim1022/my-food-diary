import json
import math
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from config.settings import UPLOAD_DIR
from frame.userapp.userapp_userdb import UserDb, PopIngrDb, RecipeDb, IngrDb, RecipeIngrDb, AllergyDb, UsersAvoidDb

import frame.mainapp.mainapp_userdb


class UserView:
    def mypage(request):
        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
        # ==================================================================
        # ==================================================================
        # ==================================================================

        context = {
            'recent': recent
        }
        return render(request, 'userapp/mypage.html', context)

    def profile(request):
        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
        # ==================================================================
        # ==================================================================
        # ==================================================================

        context = {
            'recent': recent
        }
        return render(request, 'userapp/profile.html', context)

    def userupdateimple(request):
        u_id = request.POST['id'];
        u_nick = request.POST['nick'];
        u_pwd = request.POST['reusepwd'];
        u_name = request.POST['name'];
        u_age = request.POST['age'];
        try:
            UserDb().update(u_id, u_nick, u_pwd, u_name, int(u_age))
            request.session['suser'] = u_id
            request.session['snickname'] = u_nick
        except:
            print('error');
            # ==================================================================
            # ==================================================================
            # ==================================================================
            # 최근 방문기록 가져와서 뿌려주는 코드
            recent = None
            if 'suser' in request.session:
                if request.session['suser']:
                    recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])

            context = {
                'recent': recent
            }
            # ==================================================================
            # ==================================================================
            # ==================================================================
            return render(request, 'userapp/profile.html', context);
        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])

        context = {
            'recent': recent
        }
        # ==================================================================
        # ==================================================================
        # ==================================================================
        return render(request, 'userapp/mypage.html', context);

    def ncheck(request):
        nick = request.GET['nck'];
        nicklist = UserDb().nickselect();
        if nick == '':
            return HttpResponse('0');
        elif nick not in nicklist:
            return HttpResponse('2');
        else:
            return HttpResponse('1')

    def myrecipereg(request):
        itemlist = PopIngrDb().select();
        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
        # ==================================================================
        # ==================================================================
        # ==================================================================
        context = {
            'itemlist': itemlist,
            'recent': recent
        }
        return render(request, 'userapp/myrecipe_reg.html', context)

    def myrecipeaddimpl(request):
        rc_id = request.POST['rcategory'];
        u_id = request.session['suser'];
        now = datetime.now();
        NowDateTime = now.strftime('%Y-%m-%d %H:%M:%S');
        r_regdate = NowDateTime;
        r_name = request.POST['myrtitle'];
        r_cooktime = request.POST['ctime'];

        r_kimage = [];
        r_simage = [];
        for img in request.FILES.getlist('img0'):
            r_pimage = img._name;
            r_simage.append(r_pimage);

            fp = open('%s/%s' % (UPLOAD_DIR, r_pimage), 'wb');
            for chunk in img.chunks():
                fp.write(chunk);
                fp.close();
        r_mimage = r_simage[0];

        del r_simage[0];
        for i in range(1, len(r_simage) + 1):
            r_kimage.append(i);
        r_dimage = dict(zip(r_kimage, r_simage));
        r_dimage = json.dumps(r_dimage);

        totalImgCnt = request.POST['totalImgCnt'];

        r_detail = {};
        for i in range(1, int(totalImgCnt)):
            mydi = request.POST['myrecdetail' + str(i)];
            r_detail[str(i)] = mydi;
        r_detail = json.dumps(r_detail, ensure_ascii=False);

        r_recommend = 0;
        r_view = 0;
        r_public = request.POST['public'];

        RecipeDb().insert(int(rc_id), u_id, r_regdate, r_name, r_cooktime, r_mimage, r_detail, r_dimage,
                          int(r_recommend), int(r_view), int(r_public));

        cnt = request.POST['cnt'];
        item = request.POST['iname1'];
        amt = request.POST['iamt1'];

        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
        # ==================================================================
        # ==================================================================
        # ==================================================================

        if item == None or amt == None:
            ritem = [];
            ramt = [];
            context = {
                'ritem': ritem,
                'ramt': ramt,
                'recent': recent
            }
        else:
            iid = [];
            ritem = [];
            ramt = [];
            for i in range(1, int(cnt) + 1):
                item = request.POST['iname' + str(i)];
                item = item.strip();

                amt = request.POST['iamt' + str(i)];
                amt = amt.strip();

                ingrid = IngrDb().selectone(item);

                iid.append(ingrid);
                ritem.append(item);
                ramt.append(amt);
            rzip = list(zip(ritem, ramt));
            context = {
                'iid': iid,
                'rzip': rzip,
                'ritem': ritem,
                'ramt': ramt,
                'recent': recent
            }
        return render(request, 'userapp/recipeingrcheck.html', context);

    def recipeingradd(request):
        u_id = request.session['suser'];
        iid = request.GET['iid'];
        ramt = request.GET['?ramt'];
        rid = RecipeDb().rselectone(u_id);
        ilist = list(zip(eval(iid), eval(ramt)));
        for i in ilist:
            RecipeIngrDb().insert(rid, i[0], i[1]);
        # ==================================================================
        # ==================================================================
        # ==================================================================
        # 최근 방문기록 가져와서 뿌려주는 코드
        recent = None
        if 'suser' in request.session:
            if request.session['suser']:
                recent = frame.mainapp.mainapp_userdb.RecipeDb().select_recent(request.session['suser'])
        # ==================================================================
        # ==================================================================
        # ==================================================================
        context = {
            'recent': recent
        }
        return render(request, 'mainapp/main.html', context);

    # 팝업창 항목 페이징 기능
    def popingr(request):

        # 입력 모수
        # request 요청 중 GET 방식으로 받은 사전식 자료형에서 page에 대한 값을 가져오기
        # 해당 값이 없을 경우에는 1로 설정
        page_num = request.GET.get('page', 1)
        value = request.GET.get('value', '')
        parentLocal = request.GET.get('parentLocal', '0')

        # 데이터 객체 목록을 저장하는 변수 선언
        if value == '':
            ingr = PopIngrDb().select()
        else:
            ingr = PopIngrDb().selectone(value)

        # Paginator 객체 선언
        paginator = Paginator(ingr, 15)

        # page_num의 값이 DB 데이터에서 나타낼 수 있는 범위를 넘어설 경우에는 오류가 발생
        # try ~ except로 예외를 처리: 범위를 넘어선 값에 대해선 첫 페이지로 이동

        try:
            page = paginator.page(page_num)
        except EmptyPage:
            page = paginator.page(1)

        context = {'page': page, 'parentLocal': parentLocal}
        return render(request, 'userapp/popingr.html', context)

    def allergy(request):
        algylist = AllergyDb().select();
        algychecklist = PopIngrDb().select();
        algyset = AllergyDb().allergylist();
        context = {
            'algylist': algylist,
            'algychecklist': algychecklist,
            'algyset': algyset
        };
        return render(request, 'userapp/allergy.html', context)

    def allergyrem(request):
        i_id = request.POST['aid'];
        try:
            AllergyDb().delete(int(i_id));
        except:
            return redirect('allergy');
        return redirect('allergy');

    def allergyadd(request):
        u_id = request.session['suser'];
        i_ids = request.GET.getlist('check', None);
        try:
            for i in i_ids:
                UsersAvoidDb().insert(u_id, int(i));
        except:
            return redirect('allergy');
        return redirect('allergy');

    def popsearch(request):
        ingr = request.GET['ingr'];
        ingr = ingr.strip();
        selectlist = PopIngrDb().selectone(ingr);
        if ingr == '':
            return HttpResponse('0');
        elif len(selectlist) == 0:
            return HttpResponse('1');
        else:
            context = {
                'selectlist': selectlist
            }
            return render(request, 'userapp/popingr.html')
