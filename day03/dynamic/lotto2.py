# 최종적으로 하고 싶은 것은? - 머리 속에 그리면서 진행하는 것이 좋다!
# 코딩은 항상 Divide and conquer!
# 작명 센스 배우기!
import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1'

res = requests.get(url)
dict_lotto = res.json()

winner = []

# 6개 랜덤 샘플링
for i in range(1,6,1):
    winner = random.sample(range(1,46,1), 6)

print("1등 번호는: ")
print(winner)

### 1번 확인 ###

print("당신이 뽑은 번호는 : ")
