#11659 구간 합 구하기
n,m=map(int,input().split())
dp=list(map(int,input().split()))
for i in range(n-1):
    dp[i+1]+=dp[i] #누적합 만들기
dp=[0]+dp
res=[]

for _ in range(m):
    i,j=map(int,input().split()) #구간 i,j
    tmp=dp[j]-dp[i-1]
    res.append(tmp)

for x in res:
    print(x)