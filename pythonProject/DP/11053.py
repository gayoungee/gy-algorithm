#11053 가장 긴 증가하는 부분수열
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)

dy=[0]*(n+1) #증가수열의 길이를 저장하는 dy table
dy[1]=1 #증가수열 길이 초기화
res=1

for i in range(2,n+1):
    maxLen=0
    for j in range(i-1,0,-1):
        if a[j]<a[i] and dy[j]>maxLen: #더 길게 될 수 있으면
            maxLen=dy[j]
    dy[i]=maxLen+1 #나(i)를 더한 길이 저장
    if dy[i]>res: #갱신
        res=dy[i]

print(res)