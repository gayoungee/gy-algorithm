#1929 소수 구하기
#소수는 제곱근 까지만 구하면 된다!!
import math
def solution(x):
    if x==1:
        return 0
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return 0
        return 1

m,n=map(int,input().split())
for i in range(m,n+1):
    if solution(i)==1:
        print(i)