import math
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

cnt=0
for i in range(n):
    cnt+=1
    tmp=a[i]-b
    if tmp>0:
        cnt+=math.ceil(tmp/c)
print(cnt)