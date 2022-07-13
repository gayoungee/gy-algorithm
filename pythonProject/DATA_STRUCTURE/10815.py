#10815 숫자카드

n=int(input())
card=list(map(int,input().split()))
m=int(input())
check=list(map(int,input().split()))

# 풀이 1) 시간초과
# for i in range(m):
#     if check[i] not in card:
#         print(0,end=' ')
#     else:
#         print(1,end=' ')

#사전 만들기
dic={}
for i in range(n):
    tmp=card[i]
    dic[tmp]=i

res=[0]*m
for i in range(m):
    if check[i] in dic:
        res[i]=1
    else:
        res[i]=0

for x in res:
    print(x,end=' ')
