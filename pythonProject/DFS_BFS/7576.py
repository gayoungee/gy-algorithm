# 7576 토마토
import sys
from collections import deque
m,n=map(int,input().split())
board=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    board.append(tmp)

dx=[-1,0,1,0]
dy=[0,1,0,-1]
dis=[[0]*m for _ in range(n)] #거리 표시(이 문제에선 요일)

Q=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i,j))

while Q:
    tmp=Q.popleft()
    for i in range(4):
        xx=tmp[0]+dx[i]
        yy=tmp[1]+dy[i]
        if 0<=xx<n and 0<=yy<m and board[xx][yy]==0:
            board[xx][yy]=1 #익은 토마토로 변경
            dis[xx][yy]=dis[tmp[0]][tmp[1]]+1
            Q.append((xx,yy))

max=0
for i in range(n):
    for j in range(m):
        if board[i][j]==0: #아직도 안익은 토마토가 있다면
            print(-1)
            sys.exit()
        else:
            if dis[i][j]>max:
                max=dis[i][j]

print(max)
