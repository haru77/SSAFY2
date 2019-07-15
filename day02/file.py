import os # 컴퓨터 조작할 때 가장 많이 쓰이는 라이브러리

os.listdir()

print(os.listdir())

# os.chdir(r'폴더주소')
# os.listdir

# os.rename('hello.py','dog.py')
# os.rename('dog.py', 'hello.py')

# print(os.listdir())
# os.system('touch a.txt')
# os.chdir('report')
# os.getcwd()

# 지울 때는 rm [파일명] 

# 100번 반복하며 파일을 생성
# for i in range(100,200): #(0~99까지 100개)
#     print(i)
#     # os.system('touch report' + str(i) + '.txt') # 안에서 변해가는 값을 변경해주고 싶을 떄는 삽입법을 많이 쓴다.
#     # os.system(f'touch report{i}.txt') # f string은 samsung 역량 시험에서는 사용할 수 없다.
# # f string 사용하는 방법 이외
#     os.system('touch report{}.txt'.format(i))

# os. rename('현재파일명', '바꿀파일명')

# 맨 처음에 현재 폴더에 있는 걸 다 꺼내오는 
print(os.listdir())

files = os.listdir()

# os.chdir('report')

# for name in files:
#     os.rename(name, 'samsung_' + name)

for name in files: 
    # name-'samsung_'
    # name[len('samsung_')]
    newName = str(name).replace('samsung_', 'ssafy_')    
    # files에는 뭐가 들어있을지 모르는 상황에서 name을 str으로 컴파일러에게 인식시키려면 강제 형변환을 씌워주는 방법뿐인가?
    os.rename(name, newName)

for name in files: 
    os.rename(name, name.replace('samsung_', 'ssafy_'))

    
# 네가 갖고 있는 파일 모두를..