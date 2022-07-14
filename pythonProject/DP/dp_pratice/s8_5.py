#최대 선 연결하기
#idea: 오른쪽 수열에서 최대 부분 증가 수열을 구하기
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    maxLen=0
    for j in range(i-1,0,-1):
        if a[j]<a[i] and dy[j]>maxLen:
            maxLen=dy[j]
    dy[i]=maxLen+1
    if dy[i]>res:
        res=dy[i]
print(res)