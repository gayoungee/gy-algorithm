#1697 숨바꼭질
from collections import deque
#가장 빠른 시간 => BFS
n,k=map(int,input().split())
Q=deque()
MAX=100000
dis=[0]*(MAX+1)

Q.append(n)
while Q:
  tmp=Q.popleft()
  if tmp==k:
    print(dis[tmp])
    break
  for xx in (tmp-1,tmp+1,tmp*2):
    if 0<=xx<=MAX and dis[xx]==0:
      dis[xx]=dis[tmp]+1
      Q.append(xx)