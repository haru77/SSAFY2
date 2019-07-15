import requests
#import bs4 #bs4.BeautifulSoup()
from bs4 import BeautifulSoup

# 1. op.gg에 요청을 보낸다.
url = 'https://www.op.gg/summoner/userName=cuzz'

# 2. html 응답을 받아
res = requests.get(url)

# 3. html 안에 있는 정보를 출력

doc = BeautifulSoup(res.text, 'html.parser')
win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
defeat = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses').text

# 한 번 정제를 한 데이터에서는 검색하기가 쉽다.
# browser를 통해 쉽게 구할 수 있다.

# python언어로서 얼마나 str을 다룰 수 있을지
print(win.replace("W","승")) # print(win.replace("W","")+"승")
print(defeat.replace("L","패"))