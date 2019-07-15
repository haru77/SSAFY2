from flask import Flask, render_template, request
import requests
from decouple import config
import pprint
import random

app = Flask(__name__)
token = config('TELEGRAM_TOKEN') # 전역 변수로 사용해준다.

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/send')
# def send():

#     # home에 보내온 msg를 받아 telegram api를 통해 메시지 전송
#     msg = request.args.get('msg') # home에 보내온 msg를 msg변수에 저장

#     ##
#     base="https://api.telegram.org"
#     # global token # def 내부에서 전역변수를 선언해줄 때 앞에 global을 붙인다.
#     # token = config('TELEGRAM_TOKEN')
#     method = "sendMessage"
#     method_updates = "getUpdates"
#     chat_id = "865565481"
#     text = msg # input()
#     # url1= base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text
#     url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
#     '''
#     # url을 최종적으로 보내주는 것 까지!
#     # url을 프린트해보자
#     '''
#     # 입력한 메시지를 전송하는 코드 : 링크에 url 붙여서 진행
#     requests.get(url)

#     # chat_id 가져오는 코드 
#     url_updates = f"{base}/bot{token}/{method_updates}"
    
#     #1. getUpdates메소드로 요청 보내기
#     response = requests.get(url_updates)
#     #2. 받아온 응답(jason)을 Dictionary로 바꿔서 
#     responseDict = response.json()
#     ## flask로 바로 하기보다는 python 다른 파일에서 연습을 해볼 것 같다.
#     # responseDict ["result"][]
#     resFinal = responseDict ["result"][0]["message"]["from"]["id"]
#     #url을 프린트해보자
#     return render_template('send.html', msg=msg, url=url, resFinal=resFinal)

#     # chat_id를 가져오는 코드
#     # 1. getUpdates메소드를 가져오기

@app.route(f'/{token}', methods=['POST']) # /token 페이지에서 값이 들어오면, methods 를 'POST'로 사용한다! # ? message의
def webhook():
    # 1. 메아리 챗봇
    # (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    # (2) 그대로 전송

    res = request.get_json() # 서버에서 일어나는 일들: [텔레그램에서 서버로 메시지가 날아오면, 그 메시지(를 포함한 Dictionary 정보)를 가져와서]  저장해준다.
    text = res.get("message").get("text") # 
    chat_id = res.get('message').get('chat').get('id')

    base = "https://api.telegram.org"
    method = "sendMessage"
    # method_updates = "getUpdates"
# method = 'getFile'+ '?file_id'

### 조건 분기문       
    if res.get("message").get("photo") is not None: # 이중 부정 == 긍정
        file_id = res.get("message").get("photo")[-1].get('file_id')
        file_res = requests.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get("result").get("file_path")
        file_url = f"{base}/file/bot{token}/{file_path}"
        # file path를 가져오기 위함

        url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
        #url로 보낼 거고

        image = requests.get(file_url, stream=True)

        headers = {
            config('NAVER_ID'),
            config('NAVER_SECRET'),
        }
        files = {
            'image' : image.raw.read(),
        }

        
        clova_res = requests.post(url, headers=headers, files=files)
        text = clova_res.json().get('faces')[0].get('celebrity').get('value')


        ''' 
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        response = requests.post(url,  files=files, headers=headers)
        rescode = response.status_code
        if(rescode==200):
            print (response.text)
        else:
            print("Error Code:" + rescode)
        '''


    else:
        if text == 'lotto':
            # lotto 라는 문자열이 날아오면 6개의 랜덤 숫자를 전송해준다.
            text = str(sorted(random.sample(range(1,46), 6)))
        # papago api를 활용하여 외국어 번역 서비스 삽입
        
        elif text[0:3] == "/번역": ##$$??
            # papago로 네이버 번역 결과를 알려준다.
            ##$$
            url = "https://openapi.naver.com/v1/papago/n2mt"
            headers = {
                'X-Naver-Client-Id': config('NAVER_ID'),    # .env파일에서 NAVER_ID에 해당되는 문자열값을 가져온다.
                'X-Naver-Client-Secret': config('NAVER_SECRET'),    # .env파일에서 NAVER_SECRET에 해당되는 문자열값을 가져온다.
            }
            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:],  # '/번역 댕댕이'
                                    # 0 12 34 5 6
            }
            res = requests.post(url, headers=headers, data=data)
            text = res.json()['message']['result']['translatedText']
        
    # 유명인 얼굴인식

    # 채용공고 :


    url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
    requests.get(url)

    # print(pprint( res.get("message").get("text") ))
    # print(request) # 이렇게 하면 우리 로그가 게속 찍힐 것. : 사용자가 보낸 요청에 대한 정보가 들어있다.
    # print( pprint(request.get_json())  ##$$ request.get_json() : 기능 
    # request.get("message").get("text")
    return '', 200



if __name__ == "__main__":
    app.run(debug=True)



################
    # responseDict = {} # 추가하는 식으로 사용하지 않을 거면 미리 선언 필요 없음\, 바로 dict를 받아올 수 있다.

################
# 최종 할 떄는

#  pip install python-decouple
# 이상한 거 깔게 하는 게 있다.
# 링크: https://www.zdnet.com/article/twelve-malicious-python-libraries-found-and-removed-from-pypi/

################
# 'bot'+token
# return 'webhook setup complete'