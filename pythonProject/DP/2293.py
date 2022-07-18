#2293 동전 1
n,k=map(int,input().split())
coin=[]
for _ in range(n):
    v=int(input())
    coin.append(v)

dp=[0]*(k+1)
dp[0]=1 #합이 0원이 되는 경우의 수
for i in range(n):
    for j in range(coin[i],k+1):
        dp[j]+=dp[j-coin[i]]
print(dp[k])