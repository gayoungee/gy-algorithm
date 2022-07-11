import itertools
from itertools import combinations
n,m=map(int,input().split())
card=list(map(int,input().split()))

#m과 최대한 가까운 3장의 카드를 고름
pick=itertools.combinations(card,3)

minCha=2147000000
res=0
for x in pick:
    cha=m-sum(x)
    if cha<minCha and cha>=0:
        minCha=cha
        res=sum(x)

print(res)