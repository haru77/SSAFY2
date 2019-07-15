from flask import Flask
from flask import render_template
import random as random
import requests
import bs4
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/<name>") # 뒤에 이름이 들어올거야 이야기 해줌
def hello(name):
    # name에는 /hello/ 이름/ 활용가능
    return render_template('hello.html', name=name)  # flask안에 진자라고 하는 템플릿이 하는 것.


@app.route('/menu')
def menu():
    # 랜덤으로 음식 메뉴를 추천하고,
    menu = ['양식','중식', '한식', '일식']
    result = random.choice(menu)
    
    # 해당 음식 사진을 보여주는 기능을 구현
#    recommendedMenu = { 1 :"양식", 2:"중식", 3:"한식", 4:"일식"}
    menuImgURLDict = { '양식': 'https://www.koreatimes.net/images/attach/8W9JISDEW3BPM10-2018011711010596/20180117-13013897.jpg',
                       '중식': 'http://img.etoday.co.kr/pto_db/2018/05/600/20180521163459_1214955_650_487.jpg',
                        '한식': 'https://chf.or.kr/cm_data/editorImage/201403/20140303152606.gif',
                        '일식': 'https://www.japankuru.com/prg_img/img/img2019022817331384813900.jpg?1551342793'
                    }
    # print(menuImgURLDict['중식'])
    menuImgURL=menuImgURLDict[result]
    # return menuImgURL
    return render_template('menu.html', name=result, image=menuImgURL)
    #메뉴들 묶음을 만들고, 해당하는 사진들의 주소를 찾고
'''
    구현을 할 때, 일단 쪼개서 하나부터 푼다.
    Divide and conquor***
    음식 추천 하나/ 사진 보여주는 것 하나.
'''

'''
@app.route('/lotto'):
def lotto():
    # 랜덤하게 값을 뽑고
    winner
    your_lotto
'''

if __name__ == "__main__":
    app.run(debug=True)


# 그냥 가는 파일이 아니라 템플릿을 붙여줘서 여러 템플릿을 만들 것이다.
# 템플릿 엔진은 html이랑 다르긴 하다. : 
# 템플릿 이라고 하는 폴더를 가지고, 

# app.py
# HTML 파일을 날려준다.
