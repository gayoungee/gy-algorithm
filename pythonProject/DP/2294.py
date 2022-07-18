#2294 동전 2
n,k=map(int,input().split())
coin=[]
for _ in range(n):
    v=int(input())
    coin.append(v)

dp=[100001]*(k+1)
dp[0]=0
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j]=min(dp[j],dp[j-coin[i]]+1)

if dp[k]!=100001:
    print(dp[k])
else:
    print(-1)
