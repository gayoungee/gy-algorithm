#9095 1,2,3 더하기
#f(n)=f(n-1)+f(n-2)+f(n-3)
def solution(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4

    dy=[0]*(x+1)
    dy[1]=1
    dy[2]=2
    dy[3]=4

    for i in range(4,x+1):
        dy[i]=dy[i-1]+dy[i-2]+dy[i-3]
    return dy[x]

t=int(input())
res=[]
for i in range(t):
    n=int(input())
    res.append(solution(n))
for x in res:
    print(x)