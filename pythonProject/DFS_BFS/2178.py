from collections import deque
n,m=map(int,input().split())
board=list()
for _ in range(n):
  tmp=list(map(int,input()))
  board.append(tmp)

dis=[[0]*m for _ in range(n)]
Q=deque()
dis[0][0]=1
Q.append((0,0))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
while Q:
  now=Q.popleft()
  for i in range(4):
    xx=now[0]+dx[i]
    yy=now[1]+dy[i]
    if 0<=xx<n and 0<=yy<m and board[xx][yy]==1:
      dis[xx][yy]=dis[now[0]][now[1]]+1
      board[xx][yy]=0
      Q.append((xx,yy))

print(dis[n-1][m-1])