from flask import Flask, render_template, request
from faker import Faker
import random
fake = Faker('ko_KR')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

# 바깥 쪽에 있는지 확인 : 최 상단에 두는 게 좋다고 이야고 하지만 비슷하다
names = {
    '강동주' : '외판원',
    '정의진' : '주조원',
    '이한얼' : '데이터사이언티스트',
}

@app.route('/result')
def result():
    name = request.args.get('name')
    if name in names:
        # print (str(name)+"님의 전생은 "+names[name] + " 였습니다.")
        job = names[name]
    else :
        job = job.fake()
    return render_template('result.html', job = job, name = name)#re#str(name)+"님의 전생은 "+names[name] + " 였습니다."
        
    # 1. 우리 names에 해당하는 이름이 있는지 없는지 확인

    # 2. 없다면 => 랜덤으로 fake 직업을 보여줌, names에 저장

    # 3. 있다면 => names에 저장된 직업을 보여줌

@app.route('/goonghap')
def goonghap():
    return render_template('goonghap.html')

# dict in dict
# babos = {
#     '강동주' : {
#         '김지수' : 55,
#         '아이유' : 100,
#     },
#     '이한얼' : {
#         '전여친' : 66,
#         '임수정' : 100,
#     },
# }

babos = {}
#randomNum => percent
@app.route('/destiny')
def destiny():
# 1. 쉽게
    babo = request.args.get('babo')
    you = request.args.get('you')

    name = babo+you
    if name in babos:
        randomNum = babos[babo+you]
    else :
        randomNum = random.randint(51,100)
        babos[babo+you] = randomNum
    return render_template('destiny.html', babo=babo, you=you, randomNum = randomNum)

@app.route('/opgg/search')
def opgg_search():
    return render_template('opgg_search.html')


@app.route('/opgg')
def opgg():
    import requests
    from bs4 import BeautifulSoup

    lolId = request.args.get('lolId')
    win = request.args.get('win')
    defeat = request.args.get('defeat')

    # 1. op.gg에 요청을 보낸다.
    url = 'https://www.op.gg/summoner/userName='+lolId
    # 2. html 응답을 받아
    res = requests.get(url)
    # 3. html 안에 있는 정보를 출력
    doc = BeautifulSoup(res.text, 'html.parser')
    win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    defeat = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text
    
    # 한 번 정제를 한 데이터에서는 검색하기가 쉽다.
    # browser를 통해 쉽게 구할 수 있다.

    # win[:-1]
    return render_template('opgg.html', lolId=lolId , win=win.replace("W","승"), defeat=defeat.replace("L","패") )

if __name__ == '__main__':
    app.run(debug=True)


# 2. Dict in Dict
# if babo in babos:
#     if you in babos[babo]:
#         percent = babos[babo][you]

    # return render_template('result.html', job = job, name = name)#re#str(name)+"님의 전생은 "+names[name] + " 였습니다."
        
    # 기존 dict에 있는지 확인


    # 있으면 pass

    # 없으면 dict에 A, B, random score 넣고 dict로 추가


    # 최종 출력
    # newDict = {}
    # randomNum = random.randint(51,100) # 51,101 로 써넣어야 한다.
    # newDict = {babo: {you , randomNum}}
    # return render_template('destiny.html', babo=babo, you=you, randomNum = randomNum)

# babos 있는 사람들을 모두 출력하기



# admin으로 들어가면 지금까지 넣어둔 것을 모두 가로챌(?) 수 있다. ##$$

################################

# # 이 파일로 flask 서버에서 돌릴 것
# from flask import Flask
# Flask(__name__)
# app = Flask(__name__)

# @app.route('/')
# def home(): # 작명:hompage가 될거니까 home
#     return render_template('home.html')

# @app.route('/result')
# def result():
#     name = 
#     names

# if __name__ == '__main__':
#     app.run(debug=True)

#####

        # random.sample(range(1,3),1
        # print (random.choice()) #names[random.randint(0,2)] 
#    for i in len(names): 포문으로 dict길이 만큼
    # print ( '강동주' in names)

    # nums = [1, 2, 3, 4]
    # print( 5 in nums)
