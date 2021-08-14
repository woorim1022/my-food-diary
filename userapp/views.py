import json
import math
from datetime import datetime

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
        return render(request,'userapp/mypage.html', context)

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
        return render(request,'userapp/profile.html', context)

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
            return render(request,'userapp/profile.html', context);
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
        return render(request,'userapp/mypage.html', context);

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
            'recent':recent
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
        r_mimage = '';

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
        for i in range(1, len(r_simage)+1):
            r_kimage.append(i);
        r_dimage = dict(zip(r_kimage,r_simage));
        r_dimage = json.dumps(r_dimage);

        r_detail = {};
        for i in range(1,7):
            mydi = 'myd' + str(i);
            mydi = request.POST['myrecdetail'+str(i)];
            r_detail[str(i)] = mydi;
        r_detail = json.dumps(r_detail,ensure_ascii=False);

        r_recommend = 0;
        r_view = 0;
        r_public = request.POST['public'];

        RecipeDb().insert(int(rc_id),u_id,r_regdate,r_name,r_cooktime,r_mimage,r_detail,r_dimage,int(r_recommend),int(r_view),int(r_public));

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
                'ritem':ritem,
                'ramt':ramt,
                'recent':recent
            }
        else:
            iid = [];
            ritem = [];
            ramt = [];
            for i in range(1,int(cnt)+1):
                item = 'item' + str(i);
                amt = 'amt' + str(i);
                item = request.POST['iname'+str(i)];
                item = item.strip();

                amt = request.POST['iamt'+str(i)];
                amt = amt.strip();

                ingrid = IngrDb().selectone(item);

                iid.append(ingrid);
                ritem.append(item);
                ramt.append(amt);
            rzip = list(zip(ritem,ramt));
            context = {
                'iid':iid,
                'rzip':rzip,
                'ritem':ritem,
                'ramt':ramt,
                'recent': recent
            }
        return render(request, 'userapp/recipeingrcheck.html',context);

    def recipeingradd(request):
        u_id = request.session['suser'];
        iid = request.GET['iid'];
        ramt = request.GET['?ramt'];
        rid = RecipeDb().rselectone(u_id);
        ilist = list(zip(eval(iid),eval(ramt)));
        for i in ilist:
            RecipeIngrDb().insert(rid,i[0],i[1]);
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
        return render(request, 'mainapp/main.html',context);

    def popingr(request):

        page = int(request.GET.get('page',1));

        popingr = PopIngrDb().popselect((page-1)*15);
        popuppage = (PopIngrDb().poppage()+1);

        if popuppage//5 == 0:
            allpagepart = 1;
        else:
            allpagepart = math.ceil(popuppage/5);

        if page//5 == 0:
            pagepart = 1;
        else:
            pagepart = math.ceil(page/5);

        pagelist = [];
        if allpagepart > pagepart:
            for l in range(4,-1,-1):
                pagelist.append(5*pagepart-l);
        elif allpagepart == pagepart:
            if popuppage % 5 == 0:
                for l in range(4, -1, -1):
                    pagelist.append(5 * pagepart - l);
            else:
                a = popuppage % 5;
                for l in range(1,a+1):
                    pagelist.append(5*(pagepart-1)+l);

        if allpagepart > pagepart:
            next = True;
        else:
            next = False;

        if pagepart > 1 and allpagepart > 1:
            before = True;
        else:
            before = False;
        nextnum = (pagepart * 5) + 1;
        beforenum = (pagepart - 1) * 5;
        itemlist = PopIngrDb().select();
        context = {
            'itemlist':itemlist,
            'popingr':popingr,
            'pagelist':pagelist,
            'popuppage':popuppage,
            'pagepart': pagepart,
            'next': next,
            'nextnum': nextnum,
            'before': before,
            'beforenum': beforenum
        }
        return render(request,'userapp/popingr.html',context)

    def allergy(request):
        algylist = AllergyDb().select();
        algychecklist = PopIngrDb().select();
        algyset = AllergyDb().allergylist();
        context = {
            'algylist':algylist,
            'algychecklist':algychecklist,
            'algyset':algyset
        };
        return render(request,'userapp/allergy.html',context)

    def allergyrem(request):
        i_id = request.POST['aid'];
        try:
            AllergyDb().delete(int(i_id));
        except:
            return redirect('allergy');
        return redirect('allergy');

    def allergyadd(request):
        u_id = request.session['suser'];
        i_ids = request.GET.getlist('check',None);
        try:
            for i in i_ids:
                UsersAvoidDb().insert(u_id,int(i));
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
                'selectlist':selectlist
            }
            return render(request, 'userapp/popingr.html')


    def like(request):
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
        # r_id 로 즐겨찾기 리스트 select
        u_id = request.session['suser']
        rescipe_list = RecipeDb().rselect_fav(u_id)
        # context에 담기
        context = {
            'recipe_list': rescipe_list,
            'recent': recent
        };

        return render(request, 'userapp/like.html',context)