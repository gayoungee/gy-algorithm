# 7569 토마토
import sys
from collections import deque
m,n,h=map(int,input().split()) #가로, 세로, 높이
dis=[[[0]*m for _ in range(n)] for _ in range(h)]
board=[] #가장 아래 상자부터 토마토 정보
for _ in range(h):
    box=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        box.append(tmp)
    board.append(box)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

Q=deque()
for l in range(h):
    for i in range(n):
            if board[l][i][j]==1: #익은 토마토 발견
                Q.append([l,i,j])
while Q:
    tmp=Q.popleft()
    for i in range(6):
        zz=tmp[0]+dz[i]
        xx=tmp[1]+dx[i]
        yy=tmp[2]+dy[i]
        if 0<=zz<h and 0<=xx<n and 0<=yy<m and board[zz][xx][yy]==0:
            board[zz][xx][yy]=1 #토마토는 익는다
            dis[zz][xx][yy]=dis[tmp[0]][tmp[1]][tmp[2]]+1
            Q.append([zz,xx,yy])

max=0
for l in range(h):
    for i in range(n):
        for j in range(m):
            if board[l][i][j]==0:
                print(-1)
                sys.exit()
            else:
                if dis[l][i][j]>max:
                    max=dis[l][i][j]

print(max)


