# lotto
# 스크랩은 정보제공을 

'''
요청을 해서 응답 받는 것은 h와 .. 같다. ###$$?
일반적인 웹페이지는 HTML. # 방금 받았던 파일들? 
파이썬은 json을 글자(str)로만 인지할 것.
의미를 가진 dictionary로 만들어야 한다.
'''
from flask import Flask, render_template, request
import requests
import random
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'
#

# requests.get('주소')
res = requests.get(url) # url에 있는 html 파일로부터 정보를 긁어와서 res 변수에 저장한다.
                        # requests.get 이 반환하는 자료형은 response이다. # print( type(res) )

dict_lotto = res.json() ##$$3  자료형 response으로 가져온 것 json 파일을 가져온다?
winner = []

for i in range(7):
    # list에서 값을 추가하려면 .append사용!
    winner.append(dict_lotto[f'drwtNo{i}']) ##$$? 3.6버젼 부터는 f' {i}' 보기 편하게 만들기 위해서 나온 게 format이라고 하는 str 자료형의 일종 : 
                            # 'drwtno{}.format(i)  (~python 3.5)
# 로또 랜덤 추천
your_lotto = random.sample(range(1,46), 6)

print(winner)
print(your_lotto)

# 1번째 코드
for w in winner:
    for y in your_lotto:
        if (w == y):
            count = count + 1

# 2번째 코드:set을 이용해 최적화

count = 0
trial = 0
while True:
    your_lotto = sorted(random.sample(range(1,46), 6))
 
count = len( set(your_lotto) & set(winner))

if count == 6:
    print('1등')
elif count == 5:
    print('3등')
elif count == 4:
    print('4등')
elif count == 3:
    print('5등')
else:
    print('꽝')


'''
    구현을 할 때, 일단 쪼개서 하나부터 푼다.
    Divide and conquor***
    음식 추천 하나/ 사진 보여주는 것 하나.
'''



# if __name__ == "__main__":
#     app.run(debug=True) ##$$

'''
# res.json : json 파일->python Dictionary
# print(res.json()) #( res는 하나 )
# print(res.text) 


# json_lotto = res.text ##$$
# dict_lotto = res.json() #Dict니까 키를 가지고 찾아볼 수 있음 ##$$

# winner.append(dict_lotto['drwtNo1'])
# winner.append(dict_lotto['drwtNo2'])
# winner.append(dict_lotto['drwtNo3'])
# winner.append(dict_lotto['drwtNo4'])
# winner.append(dict_lotto['drwtNo5'])
# winner.append(dict_lotto['drwtNo6'])
# winner.append(dict_lotto['drwtNo' + i ]) # 가장 무식하게라도 다 짜고 그 다음에 최적화를 하자!
'''
