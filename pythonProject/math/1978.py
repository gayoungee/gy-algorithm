#1978 소수 찾기
import math
def solution(x):
    if x==1:
        return 0
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
res=0
for x in a:
    if solution(x)==1:
        res+=1
print(res)