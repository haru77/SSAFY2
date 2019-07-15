import random as random
import requests
import bs4
from datetime import datetime
# import datetime 로 설정 시,    month = datetime.datetime.now().month # day = datetime.datetime.now().day 이렇게 2번 쳐줘야 한다.


from flask import Flask # 외부에서 깔았던 flask라는 걸 가져왔다. # flask 패키지 안에서 Flask 모듈을 썼다.**
# flask만 import해주면 flask.Flask를 일일이 써줘야 한다.
app = Flask(__name__) ##$$3?


# 1. 주문 받는 방식(어떻게)
@app.route("/") ##$$3? @는 무슨 의미? argument는?
def hello(): # 뭔가를 정의해서 쓰고 있다.
    return "Hello World!"

# 명령어 구동방식 : 1) flask run 2) Hello

# 2. 무엇을 제공할지(무엇)
@app.route("/hi")
def hi():
    return "hi"

    # 1. /name
    # 2. 여러분의 영문 이름

# decorater와 함수 정의는 붙여주는 게 좋다!
@app.route("/name")
def name(): # myName으로 해도 상관없다.
    return "Lee HanEol"

@app.route("/hello/HanEol")
def hello2():
    return "Hello, HanEol"

@app.route("/hello/<person>")
def hello3(person): # variable routing : 변수화해서 만든다
    # return person #person 이라는 통에 들어있는 값이 출력됨 
    return "Hello, " + person +"!"

# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
@app.route("/cube/<num>")
def cube(num):
    return str(int(num)** 3 ) # num을 세제곱한 값

# 1. /lotto => 랜덤 넘버 추출
@app.route("/lotto")
def lotto():
    #random number 생성
    num =[]
    num = range(1,46,1)
    # random.shuffle(num)
    result = random.choice(num)
    return str(result)

# 2. /menu => 점심 메뉴
@app.route("/menu")
def menu():
    menu = ['중식', '일식', '양식', '한식']
    result = random.choice(menu)
    return str(result)

# 3. /kospi => 현재 네이버 기준 kospi
@app.route("/kospi")
def kospi(): 
    url = "https://finance.naver.com/sise/"
    response = requests.get(url).text # res 줄임말로도 많이 쓰는데, FullName을 써서 누가 보더라도 알 수 있게 하는 게 더 좋은 컨벤션이긴 하다.
    document = bs4.BeautifulSoup(response , 'html.parser') # 'html.parser'의 의미?##$$
    kospi = document.select_one('#KOSPI_now').text # id가 #KOSPI_now 인 것을 뽑아오기
    return "현재 kospi는" + str(kospi) + " 입니다."

# /newyear
@app.route("/newyear")
def newyear():
    # today = datetime.datetime.now()
    # return str(today)
    month = datetime.now().month
    day = datetime.now().day
    if month == 1 and day == 1:
        print("이건 프린트")
        return "<h1>예</h1>"
    else:
        return "<h1>아니요</h1>"

    # 만약 오늘이 1월 1일이라면,
    # if today
    #   예
    # 아니면
    #   아니요


    # return str(month) + "월 " + str(day) + "일"
    # 어떻게 하면 일부만 뽑아올 수 있을까? slicing : 쉽게 뽑아올 수 있는 방법이 있을 듯
    # year, month, day, hour

    # 콘솔 창에 나온다.


'''
1. 인사 하는 기능

Terminal에서 / 의미 : root
$ cd /
student@M701 MINGW64 /
$ pwd
/
'''

'''
<span
style="
font-style: italic ; 
font-weight: bold; 
font-size: 1.5em;
line-height: 1.0em; 
color: navy;
font-family: arial;
">
'''