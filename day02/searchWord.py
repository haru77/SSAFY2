import requests
import bs4

'''
1. 1위 검색어 가져오기
2. 상위 검색어 10개 검색어 가져오기
-> select 사용해보기
'''

'''
first code
'''

url = 'https://www.naver.com/'
response = requests.get(url).text
document = bs4.BeautifulSoup(response, 'html.parser') # argument 정리하기 ##$$
#rank = document.select_one('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
rank = document.select('.ah_k') #.ah_k를 찾아내는 방법 ##$$

# print(rank)
# print(rank[2].text)

# 상위 검색어 10개 출력
for item in rank:
    print(item.text)


'''
second code (error)
'''

# url = 'https://www.naver.com/'

# response = requests.get(url).text

# document = bs4.BeautifulSoup(response, 'html.parser') # argument 정리하기 ##$$

# searchWord = document.select_one('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text


# print (searchWord)

# searchWords = []
# for i in range (10):
#     searchWords[i-1] = document.select_one('ul.ah_l:nth-child(5) > li:nth-child('+str(i)+') > a:nth-child(1) > span:nth-child(2)').text

# for i in range (10):
#     # print ( '%d위 검색어는 %s 입니다!' %i %searchWords[i-1] )
#     print(searchWords[i])

# ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)

# print(searchWord)
# print(document)
# print(response)
#.ah_on > a:nth-child(1) > span:nth-child(2)