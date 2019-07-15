import requests
from decouple import config
from pprint import pprint

url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    'X-Naver-Client-Id': config('NAVER_ID'),    # .env파일에서 NAVER_ID에 해당되는 문자열값을 가져온다.
    'X-Naver-Client-Secret': config('NAVER_SECRET'),    # .env파일에서 NAVER_SECRET에 해당되는 문자열값을 가져온다.
}
data = {
    'source': 'ko',
    'target': 'en',
    'text': '띵작',
}
res = requests.post(url, headers=headers, data=data)
pprint(res.json())

print(res.json()['message']['result']['translatedText'])

# ['message']['result'][]
#.get:가져오다
#.post:게시하다. (보내다)