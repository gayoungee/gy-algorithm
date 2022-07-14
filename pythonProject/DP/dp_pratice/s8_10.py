# 동전 교환
n=int(input()) #동전의 종류 개수
coin=list(map(int,input().split()))
m=int(input()) #거슬러줄 금액

#동전을 가치 개념으로 생각하기
dy=[1000]*(m+1) #큰 수로 초기화 해두기
dy[0]=0
for i in range(n):
    for j in range(coin[i],m+1):
        dy[j]=min(dy[j],dy[j-coin[i]]+1)
print(dy[m])