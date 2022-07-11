#최대 부분 증가 수열
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0) # 인덱스 1번부터 시작하도록 하려고 삽입
dy=[0]*(n+1)
dy[1]=1
res=0

for i in range(2,n+1):
    maxLen=0
    for j in range(i-1,0,-1):
        # 일단 자기(a[i]) 보다 작아야하고 더 길게 될 수 있는 경우를 찾는다
        if a[j] < a[i] and dy[j] > maxLen:
            maxLen=dy[j]
    dy[i]= maxLen + 1
    if dy[i]>res:
        res=dy[i] #최댓값 갱신

print(res)