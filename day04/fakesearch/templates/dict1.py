# import random

# nums = [1,2,3,4]

# names = {
#     '강동주' : '외판원',
#     '정의진' : '주조원',
#     '이한얼' : '데이터사이언티스트',
#     '양찬우' : '프로그래머',
# }
# print('김민지' in names)

# names['양찬우'] = '프로그래머'
# print(type(names.keys()))

# # dict in dict
# babos = {
#     '강동주' : {
#         '김지수' : 55,
#         '아이유' : 100
#     }
# }
# # 이름 두개 응
# # dict in dict

# # print(babos['강동주']['김지수'])


# babos = {
#     '강동주' : {
#         '김지수' : 55,
#         '아이유' : 100,
#     },
#     '이한얼' : {
#         '전여친' : 66,
#         '임수정' : 100,
#     },
# }

# babo = '강동주'
# you = '김지수' 

# # 기존 dict에 있는지 확인

# # 있으면 pass

# # 없으면 dict에 A, B, random score 넣고 dict로 추가

# # 최종 출력
# # newDict = {babo: {you , randomNum}}


# # for babo in babos:
#     # # for you in babo:
#     # print(babos[babo]) # 해당되는 value값 출력하기

# # babos[babo] : dict안에 dict가 출력됨
# # babos[babo][dict안의 dict의 키]


# for k, v in babos.items():
#     print(k,v)
# # key만 뽑는 방법
# print(list(babos.keys))
# # values만 뽑는 방법
# print(list(babos.values))