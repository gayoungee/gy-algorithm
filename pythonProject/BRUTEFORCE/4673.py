#4673 셀프 넘버
#그수 + 그 수의 자릿수를 다 더한거
def solution(n):
    res = n
    while n>0:
        res+=n%10
        n=n//10
    return res

num = list(range(0,10002))
res=[]
for i in range(1,10002):
    tmp=solution(num[i])
    if tmp<10001:
        res.append(tmp)

for i in range(1,10001):
    if i not in res:
        print(i)