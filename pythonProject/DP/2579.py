#2579 계단 오르기
#런타임 에러 안나게 문제 조건만큼 리스트 잡아놓을것!!!
n=int(input())
steps=[0]*301
for i in range(n):
    tmp=int(input())
    steps[i]=tmp

dp=[0]*301
dp[0]=steps[0]
dp[1]=steps[0]+steps[1]
dp[2]=max(steps[1]+steps[2], steps[0]+steps[2])

for i in range(3,n):
    dp[i]=max(dp[i-3]+steps[i-1]+steps[i], dp[i-2]+steps[i])

print(dp[n-1])