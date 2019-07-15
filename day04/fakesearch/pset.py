# '''
# Python dictionary 연습 문제
# '''
# '''
# # 1. 평균을 구하시오.
# score = {
#     '수학': 80,
#     '국어': 90,
#     '음악': 100
# }

# # 아래에 코드를 작성해 주세요.

# print(score.keys())
# print(list (score.values()) )
# print(score.items())
# print('==== Q1 ====')
# sum = 0
# for i in list(score.values()):
#     sum += i
# sum /= len(list (score.values()))
# print (sum)



# # 2. 반 평균을 구하시오. -> 전체 평균
# scores = {
#     'a': {
#         '수학': 80,
#         '국어': 90,
#         '음악': 100
#     },
#     'b': {
#         '수학': 80,
#         '국어': 90,
#         '음악': 100
#     }
# }

# # 아래에 코드를 작성해 주세요.
# print('==== Q2 ====')

# # result = {}
# # for i in list(scores.keys()):
# #     sum(list(scores[i].values))/ len(list(scores[i].values))
# #     for j in list(scores[i].keys()):
#         # result[i] += scores[i][j]
# resFinal = 0
# resSum = 0
# for i in list(scores.keys()):
#     for j in list (scores[i].keys()):
#         resSum += scores[i][j] 
#     resFinal += resSum/len(list (scores[i].keys()))
#     resSum = 0
# print (resFinal)

# # 3. 도시별 최근 3일의 온도입니다.
# city = {
#     '서울': [-6, -10, 5],
#     '대전': [-3, -5, 2],
#     '광주': [0, -2, 10],
#     '부산': [2, -2, 9],
# }
# '''
# '''
# # 3-1. 도시별 최근 3일의 온도 평균은?
# resFinal = 0
# # 아래에 코드를 작성해 주세요.
# print('==== Q3-1 ====')
# for i in list(city.keys()):
#     # resFinal += sum(list(city[i])) / len(list(city[i]))
#     print(i)
# print(resFinal)

#   '''
# # 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# #비교하는 대상 자체에서 : list안에 list라서 바로 뽑기 어려운데, 하나의 리스트로 쭉 뽑으면 왠지 다 됐을 것 같다.
# # flatten을 하려고..

# # 아래에 코드를 작성해 주세요.
# # print('==== Q3-2 ====')
# # resFinal = 0
# # resSum = 0
# # maxValue = 0
# # minValue = 0
# # for i in list(city.keys()):
# #     if (max( list (city[i])) >= maxValue)
# #         maxValue = max( list (city[i]))
#     # if

# # for i in list()
# ''' 
# # 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# # 아래에 코드를 작성해 주세요.
# print('==== Q3-3 ====')
# '''


# '''
# # 정답
# # 1.
# res = 0
# res = sum(score.values())/len(score.values())

# # 2.

# # 3-1. 
# for temp in city.values():
#     print(sum(temp)/len(temp))

# # 3-2.
# # print(max(city.values()))
#  # print(max(temp))
# maxes = []
# mins = []
# for temp in city.values():
#     maxes.append(max(temp))
#     mins.append(min(temp))
# print(max(maxes))
# print(min(mins))

# high = max(maxes)
# low = min(mins)

# for key, value in city.items():
#     if high in value:
#         print(key)
#     if low in value:
#         print (key)

# # 3-3.
# # if 영상 2도인 게 있었는가?
# if 2 in city['서울']:
#     print(True)
# else:
#     print(False)
# # iter tools를 쓰면 편하게 할 수 있다.

# '''