# import requests
# import bs4
# import numpy as np
# import random 

# # i=1
# # print ('ul.ah_l:nth-child(5) > li:nth-child('+str(i)+') > a:nth-child(1) > span:nth-child(2)' == 'ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)' )

# # name = 'samsung_report'
# # print ( name - 'report' )


# # replace
# list1 = []
# list1 = list(range(1,16))
# list1 = random.shuffle(list1)
# print( list1 )

# print(3**3)

# result = "양식"
# menuImgURLDict = {"양식": 'https://encrypted-tbn0.gstatic.com/images=tbn:ANd9GcRYdQ6ZX5h8mkVbp1zQurgwd4EzyAfUPO949fF_Vv74lQh-VWR6',
#                 "중식": 'http://img.etoday.co.kr/pto_db/2018/05/600/20180521163459_1214955_650_487.jpg',
#             #   "한식": 'https://chf.or.kr/cm_data/editorImage/201403/20140303152606.gif',
#             #   "일식": 'http://postfiles12.naver.net/MjAxNzA2MDhfMjgy/MDAxNDk2ODQ4OTgyNTkz.STv8ceNDC7achQY9VW4pGuVYRdhGUOiifEmsotRtnXsg.Z4RJC7SBwSebvNLv96DlX5-3D4AF2tr_vjPVLy_4wikg.JPEG.tjduswn3577/IMG_6049.JPG?type=w773'
#                 }
# menuImgURL=menuImgURLDict[result]

menuImgURLDict = { '양식': 'https://encrypted-tbn0.gstatic.com/images=tbn:ANd9GcRYdQ6ZX5h8mkVbp1zQurgwd4EzyAfUPO949fF_Vv74lQh-VWR6',
                   '중식': 'http://img.etoday.co.kr/pto_db/2018/05/600/20180521163459_1214955_650_487.jpg',
                   '한식': 'https://chf.or.kr/cm_data/editorImage/201403/20140303152606.gif',
                   '일식': 'http://postfiles12.naver.net/MjAxNzA2MDhfMjgy/MDAxNDk2ODQ4OTgyNTkz.STv8ceNDC7achQY9VW4pGuVYRdhGUOiifEmsotRtnXsg.Z4RJC7SBwSebvNLv96DlX5-3D4AF2tr_vjPVLy_4wikg.JPEG.tjduswn3577/IMG_6049.JPG?type=w773'
                }
print(menuImgURLDict['중식'])