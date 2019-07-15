import requests
from decouple import config

''' 
# 1. 미리 테스트 해보기 : sendMessage
base="https://api.telegram.org"
token = "bot"+config(TELEGRAM_TOKEN)
method = "sendMessage"
chat_id = "865565481"
text = "하이하이" # input()
# url1= base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text
url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"

response = requests.get(url)
print(response)
'''

'''
# 2. 미리 테스트 해보기 : getUpdates
# pprint(), python
base="https://api.telegram.org"
token = 'bot'+config("TELEGRAM_TOKEN")
method = "sendMessage"
method_updates = "getUpdates"
chat_id = "865565481"

# chat_id 가져오는 코드 
url = f"{base}/{token}/{method_updates}"
#1. getUpdates메소드로 요청 보내기
response = requests.get(url)
#2. 받아온 응답(jason)을 Dictionary로 바꿔서 
responseDict = response.json()
## flask로 바로 하기보다는 python 다른 파일에서 연습을 해볼 것 같다.
resFinal = responseDict ["result"][0]["message"]["from"]["id"]


response = requests.get(url)
print(response)
# print(responseDict)
print(resFinal)
'''



# 3. 미리 테스트 해보기 : .env
# home에 보내온 msg를 받아 telegram api를 통해 메시지 전송
# msg = request.args.get('msg') # home에 보내온 msg를 msg변수에 저장
msg ="하이하이"
##
base="https://api.telegram.org"
token = config('TELEGRAM_TOKEN')
method = "sendMessage"
method_updates = "getUpdates"
chat_id = "865565481"
text = msg # input()
# url1= base + token + method + "?" + "chat_id=" + chat_id + "&" + "text=" + text
url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"
'''
# url을 최종적으로 보내주는 것 까지!
# url을 프린트해보자
'''
# 입력한 메시지를 전송하는 코드 : 링크에 url 붙여서 진행
requests.get(url)

# chat_id 가져오는 코드 
url_updates = f"{base}/{token}/{method_updates}"


#1. getUpdates메소드로 요청 보내기
response = requests.get(url_updates)
#2. 받아온 응답(jason)을 Dictionary로 바꿔서 
responseDict = response.json()
## flask로 바로 하기보다는 python 다른 파일에서 연습을 해볼 것 같다.
# responseDict ["result"][]
resFinal = responseDict ["result"][0]["message"]["from"]["id"]
#url을 프린트해보자
print(resFinal)

#############################
# +text
# 숨기는 방법도 배우기 : 
# 224026642
# "first_name": "ssafy2"
# "username": "ssafy2_bot"



###############################
# "getMe"
# "getUpdates"
# "sendMessage?chat_id=865565481&text=에라이"
# my_id="868326205"



############################### ##$$
# def내부에 있는 변수를 전역변수로 미리 빼놓고 form에다가 미리 써놓을 수 있을까?
# def내부에서 전역변수 선언하고 싶을 때는 global을 붙여준다. 그러나
# 그러나 바로 대입은 안되므로
# global chat_id
# chat_id = "하루" # 이렇게 선언 해주어야 한다.

###############################
# git에서 이건 절대 무시해라 : 앞으로 git으로 관리 안 할테니 무시해줘!