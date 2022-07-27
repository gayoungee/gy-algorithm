#11279 최대 힙
import heapq
maxHeap=[]
n=int(input())
num=[]
for _ in range(n):
    x=int(input())
    num.append(x)
for x in num:
    if x==0:
        if maxHeap:
            print(-1*heapq.heappop(maxHeap))
        else:
            print(0)
    else:
        heapq.heappush(maxHeap,-x)