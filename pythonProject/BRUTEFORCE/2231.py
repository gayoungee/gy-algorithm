#2231 분해합
def SumFn(x):
    sum=0
    while True:
        if x<10:
            sum+=x
            return sum
        sum+=x%10
        x=x//10
    return sum

res=list()
n=int(input())
for i in range(n-1,0,-1):
    tmp=i+SumFn(i)
    if tmp==n:
        res.append(i)

if len(res)==0:
    print(0)
else:
    print(min(res))