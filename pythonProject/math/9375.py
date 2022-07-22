#9375 패션왕 신해빈
from itertools import combinations
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