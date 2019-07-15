'''
# 1. problem.txt 파일을 생성 후, 다음과 같은 내용을 작성
0
1
2
3

# 2. problem.txt의 파일 내용을 다음과 같이 변경
3
2
1
0
'''
'''
# 3. reverse.txt의 파일 내용에 problem.txt의 파일 내용을 반대로 넣기
lineNum = 0 
textContents = []
with open( 'problem.txt', 'r') as f:
    while ( (textContents[lineNum] = f.readline()) !=  ''  ):
        lineNum = lineNum + 1

print (lineNum)
'''

'''
# 1
with open( 'problem.txt', 'w' ) as f:
    for i in range (0,4):
        f.write (str(3-i) + '\n' )
'''
#2 
textContents = []
with open( 'problem.txt', 'r') as f:
    # for i in range(3):
    while((textContents[i] = f.readline()) != '' ):

# EOF error 의 경우 try catch문으로도 잡을 수 있다.         


with open( 'problem.txt', 'w') as f:
    for i range(3):
        f.write(str(textContext[lineNum-i]) + '\n' )

#        f1.write(content + "\n")
