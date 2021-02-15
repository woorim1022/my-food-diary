import datetime

import requests
from bs4 import BeautifulSoup
import re
import os

# pip install requests, bs4, lxml 필요
# import는 re(정규식) os(시스템)
from frame.scraping.scpclass import RecipeDb, IngrDb

titlelist = {}  # 제목 특수문자 제외
titlename = {}  # 제목원본
mimagelist = {} # 대표이미지 경로
errorlist = []  # 에러난 제목
timelist = {}  # 시간
steplist = {}  # 조리순서
dimagelist = {} #이미지 경로
now = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S') #현재시간
allnum =120; #레시피번호
ingrnum = 0; #식재료번호
for i in range(1,6):  # 페이지 돌리기
    url1 = "https://www.10000recipe.com/recipe/list.html?order=reco&page={}".format(i)  # url 설정 포맷형식으로 1페이지, 2페이지... 지정
    # user-agent 설정(사용자 정보 전송)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

    res1 = requests.get(url1, headers=headers)  # url1에서 가져온 정보를 res1에 저장
    res1.raise_for_status()  # 제대로 가져와지는지 확인 명령어

    soup1 = BeautifulSoup(res1.text, "lxml")  # bs4객체 생성 lxml지정(lxml: html 파서(xml 해석 프로그램))

    # select를 통해 div 클래스 지정하여 찾아옴
    recipe = soup1.select('div.common_sp_thumb')

    for idx, r in enumerate(recipe):  # 페이지 내 레시피 링크 들어가기
        allnum += 1;
        link = r.select_one("a.common_sp_link")  # 링크 url 긁어오기

        url2 = "https://www.10000recipe.com/" + link.attrs["href"]  # url이 일부만 되어있어서 앞에부분 추가

        res2 = requests.get(url2, headers=headers)  # 완성된 url에 있는 정보 긁어오기
        res2.raise_for_status()

        soup2 = BeautifulSoup(res2.text, 'lxml') # bs4객체 생성 lxml지정(lxml: html 파서(xml 해석 프로그램))

        # 제목 따오기 및 mimage 경로 딕셔너리 만들기
        try:
            title = soup2.select("div.view2_summary > h3")[0]  # 긁어온 정보의 해당 위치의 정보 담기
            text = title.get_text()  # 담은 정보의 텍스트만 가져오기
            titlename[i * 100 + idx] = title.get_text()  # 제목원본 딕셔너리에 담기(i는 페이지 idx는 레시피)
            titlelist[i * 100 + idx] = re.sub('[()"-=,.?/:$*%]', '', text)  # 제목에서 특수문자를 제외하기위한 정규식(re)
            # mimagelist[i * 100 + idx] = "static/assets/img/mimage/"+titlelist[i*100+idx] +".jpg" #메인이미지 경로
        except:  # 에러날시 에러리스트에 추가
            errorlist.append(titlelist[i * 100 + idx])
            print(titlelist[i * 100 + idx])
            print('제목')

        #대표 이미지 가져오기
        # try:
        #     image = soup2.select('div.centeredcrop > img')[0]
        #     image_url = image["src"] #src속성 가져오기(url)
        #     image_res = requests.get(image_url)
        #     image_res.raise_for_status()
        #     with open("c:/4조 폴더/my-food-diary/static/assets/img/fimage/{}.jpg".format(titlelist[i*100+idx]),"wb") as f: #mimage폴더에 파일 생성
        #         f.write(image_res.content) #파일에 이미지 저장
        # except:
        #     errorlist.append(titlelist[i * 100 + idx])
        #     print(titlelist[i * 100 + idx])
        #     print('메인이미지')

        #조리시간 가져오기
        # try:
        #     time = soup2.select('span.view2_summary_info2')[0]
        #     timelist[i*100+idx]= time.get_text()
        # except:
        #     errorlist.append(titlelist[i * 100 + idx])
        #     print(titlelist[i * 100 + idx])
        #     print('시간')

        #조리순서 내용 및 dimage 경로 딕셔너리 만들기
        cnt= 0 #순서가 몇까지 있는지 확인하기위한 변수
        step = soup2.select('div.view_step_cont')
        try:
            for snum,s in enumerate(step):
                details = s.get_text().replace('\n','')
                # detail = re.sub('"', '', details)
                # print(detail)
                if cnt == 0:
                    #첫번째 실행 시 딕셔너리안에 벨류값을 리스트형태로 생성 {key: [value]}
                    steplist[i*100+idx] = {details:"static/assets/img/dimage/"+titlelist[i*100+idx] +"/{}.jpg".format(snum+1)}
                    # dimagelist[i*100+idx] = {str(snum+1):"static/assets/img/dimage/"+titlelist[i*100+idx] +"/{}.jpg".format(snum+1)}
                    cnt +=1
                else: #첫번째 제외 벨류값리스트에 추가

                    steplist[i*100+idx
                    ][details] = "static/assets/img/dimage/"+titlelist[i*100+idx] +"/{}.jpg".format(snum+1)
                    # dimagelist[i*100+idx][str(snum+1)] = "static/assets/img/dimage/"+titlelist[i*100+idx] +"/{}.jpg".format(snum+1)
                    cnt +=1
            RecipeDb().update(str(steplist[i * 100 + idx]).replace("\'","\""),titlelist[i * 100 + idx])
        except:
            errorlist.append(titlelist[i * 100 + idx])
            print(titlelist[i * 100 + idx])
            print('조리순서 or 상세이미지경로')
        #조리순서 이미지 가져오기
        # for l in range(0,cnt): # 조리순서 총갯수만큼 반복
        #     try:
        #         soup2.select('div#stepimg{} > img'.format(l+1))[0]
        #         step_image = soup2.select('div#stepimg{} > img'.format(l+1))[0] # #은 아이디지정할때 씀 class는 . 하위태그는 >
        #         step_image_url = step_image["src"]
        #         step_image_res = requests.get(step_image_url)
        #         step_image_res.raise_for_status()
        #         path = 'c:/4조 폴더/my-food-diary/static/assets/img/fimage/{}'.format(
        #             titlelist[i * 100 + idx])  # 폴더 생성 경로 및 이름 지정
        #         os.makedirs(path, exist_ok=True)  # 폴더생성 명령어 exist_ok=True는 폴더가 이미 있을 시엔 생성안함
        #         with open(
        #                 "c:/4조 폴더/my-food-diary/static/assets/img/fimage/{}/{}.jpg".format(titlelist[i * 100 + idx],(l+1)),
        #                 "wb") as f:
        #             f.write(step_image_res.content)
        #     except:
        #         errorlist.append(titlelist[i * 100 + idx])
        #         print(titlelist[i * 100 + idx])
        #         print('스탭이미지' +str(l+1))

        # 레시피에 따른 식재료 가져오기
        # ingrs = soup2.select('div.ready_ingre3 > ul > a > li')
        # try:
        #     for ingr in ingrs: #inum은 한 레시피에 여러 식재료가 담기기때문에 불러오기위한 숫자
        #         ingrnum += 1 #ingr테이블에 저장하기 위한 숫자
        #         ingrid= ''
        #         ingr_q = ''
        #         ingrname = ingr.get_text()
        #         ingrname = ingrname[:ingrname.find(' ')] #식자재 이름
        #         ingr_q = ingr.get_text()
        #         ingr_q = ingr_q[ingr_q.rfind(' '):].strip() #식자재 분량
        #         if ingrname not in IngrDb().select(): #ingr테이블에 식자재가 없을 경우
        #             IngrDb().insert(ingrnum,1,ingrname) #ingr테이블에 식자재 저장
        #         ingrid = IngrDb().select_id(ingrname) #식자재이름으로 식자재번호 불러오기
        #         RecipeDb().ingr_insert(allnum,ingrid,ingr_q) #레시피별 식자재저장
        # except:
        #     errorlist.append(titlelist[i * 100 + idx])
        #     print(str(allnum))
        #     print(titlelist[i * 100 + idx])
        #     print('식재료 저장 or 레시피별식재료 저장')

        #레시피 DB에 저장
        # try:
        #     RecipeDb().insert(allnum,1,None,now,titlelist[i * 100 + idx],timelist[i * 100 + idx],mimagelist[i * 100 + idx],str(steplist[i * 100 + idx]).replace("\'","\""),str(dimagelist[i * 100 + idx]).replace("\'","\""),0,0,1)
        # except:
        #     errorlist.append(titlelist[i * 100 + idx])
        #     print(titlelist[i * 100 + idx])
        #     print('레시피저장')

# print(titlelist[111])  # 제목 특수문자 제외
# print(titlename[111])  # 제목원본
print(errorlist) # 에러난 제목
# print(timelist[111])  # 시간
# print(str(steplist[111]).replace("\'","\""))  # 조리순서
# print(str(dimagelist[111]).replace("\'","\""))  # 조리순서
# print(ingrnamelist[111])  # 레시피에 따른 재료
# print(ingr_qlist[111])  # 재료별 분량
# print(mimagelist[111])

# RecipeDb().insert(111,1,None,now,titlelist[111],timelist[111],mimagelist[111],str(steplist[111]).replace("\'","\""),str(dimagelist[111]).replace("\'","\""),1,1,1)