#1012 유기농 배추
import sys
sys.setrecursionlimit(2500*50*50)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y):
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and board[xx][yy]==1:
            board[xx][yy]=0
            DFS(xx,yy)

t = int(input())
res=[]
for test in range(t):
    n, m, k = map(int, input().split())  # 가로, 세로, 배추 위치 개수
    board = [[0] * m for _ in range(n)]
    cnt=0
    for _ in range(k):
        x,y=map(int,input().split())
        board[x][y] = 1 #배추 심기
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                cnt+=1
                board[i][j]=0
                DFS(i,j)
    res.append(cnt)

for x in res:
    print(x)