# 외장이므로 가져와줘야 한다.

import webbrowser
#webbrowser.open("www.naver.com")

keyword = "임수정"
keywords = ["아이유", "수지", "설현", "임수정"]
url = "https://search.daum.net/search?q="

# webbrowser.open(url+keyword)
for keyword in keywords:
    webbrowser.open(url+keyword)
