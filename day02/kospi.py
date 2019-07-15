import requests
import bs4

# 클래스 이름은 파스칼로 쓴다.
# 언더바를 지양한다. (함수명 빼고는)
# 작명 센스 ## ?

# url = "https://www.daum.net/" #http 뒤에 s가 반드시 들어가야 한다.
url = "https://finance.naver.com/sise/"
url_ex = "https://finance.naver.com/marketindex"

response = requests.get(url).text # res 줄임말로도 많이 쓰는데, FullName을 써서 누가 보더라도 알 수 있게 하는 게 더 좋은 컨벤션이긴 하다.
response_ex = requests.get(url_ex).text

document = bs4.BeautifulSoup(response , 'html.parser') # 'html.parser'의 의미?##$$
document_ex = bs4.BeautifulSoup(response_ex , 'html.parser')

# 자동 완성 기능으로  메서드 이름을 보고 기능에 대해서 추론하기

'''
# type (requests.get(url))
print(response) # 뭔가를 가져와줘 #test로 가져와줘
# print(requests.get(url).text)
'''

kospi = document.select_one('#KOSPI_now').text # id가 #KOSPI_now 인 것을 뽑아오기
kosdaq = document.select_one('#KOSDAQ_now').text
kospi200 = document.select_one('#KPI200_now').text
usd = document_ex.select_one('.usd > div:nth-child(2) > span:nth-child(1)').text


print('현재 코스피 지수는 : ' + kospi)
print('현재 코스닥 지수는 : ' + kosdaq)
print('현재 코스피200 지수는 : ' + kospi200)
print('현재 원-달러 환율은 : ' + usd)



# html = urllib.request.urlopen(url)
# source = html.read()


'''
def get(maxCount = 1):
    imgUrl = "" # 이미지 url과 조합하여 다운받을 주소
    url = ""

    count = 1
    while count <= max_count :
        print("********** [ %d번째 이미지 ] ************ " % count)
        html = urllib.request.urlopen(url)
        source = html.read()
'''


#edu ssafy page에 내용을 긁어와서 아예 가져오기..
#사진이 그대로 들어온다.
# 자바로 짜면 30줄 넘는다.
# 실행 전에 저장하기


#</body>
#</html>

# html -> DOM(?)이라는 문서 구성 장치 알아야 -> 돔트리 -> 

# 우리한테 
# 예쁘게 만든다
#beautiful