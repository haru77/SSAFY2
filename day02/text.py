
# f = open('ssafy.txt', 'w') # f : file # open을 통해 r, w, a를 수행하면, 수행 후에 객체가 리턴값으로 나온다.
# print(f)
# for i in range(5):
#     f.write('hello ssafy\n')
# f.close() # 파일은 열고 나서는 닫아야 한다.

'''
# open 앞에 with
with open("ssafy.txt",'w', encoding = 'utf-8') as f : # as : 지정해주는 코드, 이니셜 같은 것
    for i in range(5):
        f.write('with를 썼다\n')
'''

with open('ssafy.txt', 'r') as f: # f라고 하는 상자에 넣어서 쓰겠다.
    # encoding = 'utf-8' 로 설정하면 왜 오히려 안될까? ##$$
    # result = f.read()

    # 한 줄 한 줄 읽어와서 변경하거나 추가를 하거나 수정을 할 때..
    result = f.readlines()
    print(result)

f.close() 