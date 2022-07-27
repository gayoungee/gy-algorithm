#1927 최소 힙
import heapq
minHeap=[]
n=int(input())
num=[]
for _ in range(n):
    x=int(input())
    num.append(x)
for x in num:
    if x==0:
        if len(minHeap):
            print(heapq.heappop(minHeap))
        else:
            print(0)
    else:
        heapq.heappush(minHeap,x)