#15989 1,2,3 더하기 4
def solution(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 3
    else:
        dp = [1] * (x + 1) # 1만 써서 합을 나타내는 방법은 공통
        for i in range(2,x+1):
            dp[i]+=dp[i-2] #2를 사용하는 경우 추가
        for i in range(3,x+1):
            dp[i]+=dp[i-3] #3을 사용하는 경우 추가
    return dp[i]

t=int(input()) #테스트 케이스
test=[]
for i in range(t):
    n=int(input())
    test.append(n)

for i in range(t):
    print(solution(test[i]))