# 10815 숫자 카드 2
n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

nlist.sort()
#1. 빈도 정렬
dic={}
for x in nlist:
    if x in dic:
        dic[x]+=1
    else:
        dic[x]=1

for i in range(m):
    if mlist[i] in dic:
        print(dic[mlist[i]],end=' ')
    else:
        print(0,end=' ')