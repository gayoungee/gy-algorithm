# 1181 단어 정렬
n=int(input())
word=[]
for i in range(n):
    tmp=input()
    size=len(tmp)
    word.append([tmp,size])

word.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    if i==0:
        print(word[i][0]) #처음껀 무조건 출력
    else:
        if word[i-1][0]==word[i][0]: #그 이전단어와 동일하면
            pass
        else:
            print(word[i][0])
