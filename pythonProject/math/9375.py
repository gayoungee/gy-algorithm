#9375 패션왕 신해빈
#(카테고리 1 종류수+1) * (카테고리 2 종류수+1) * ... * (카테고리 n 종류수+1) - 1
#각 카테고리를 선택하지 않을 경우를 대비해 +1 을 해주고, 마지막에 -1 빼주는건 아무 카테고리도 선택하지 않았을때를 대비하기 위함
t=int(input())
resList=[]
for i in range(t):
    dic={}
    n=int(input())
    for j in range(n):
        name,type=input().split(' ')
        if type in dic:
            dic[type]+=1
        else:
            dic[type]=1
    res=1
    for x in dic:
        res*=(dic[x]+1)
    resList.append(res-1)

for x in resList:
    print(x)