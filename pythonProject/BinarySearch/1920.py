# 1920 수 찾기
n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

nlist.sort() #이분 탐색 전제조건은 정렬!
def solution(x):
    lt=0
    rt=n-1
    while lt<=rt:
        mid=(lt+rt)//2
        if nlist[mid]==x:
            return 1
        elif nlist[mid]<x:
            lt=mid+1
        elif nlist[mid]>x:
            rt=mid-1
    return 0

for i in range(m):
    print(solution(mlist[i]))
