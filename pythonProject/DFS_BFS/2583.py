#2583 영역 구하기
import sys
sys.setrecursionlimit(10001)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<m and board[xx][yy]==0:
            cnt+=1
            board[xx][yy]=1 #벽으로 만들고
            DFS(xx,yy)

m,n,k=map(int,input().split())
board=[[0]*m for _ in range(n)]

#직사각형 색칠하기
for _ in range(k):
    lx,ly,rx,ry=map(int,input().split())
    for row in range(lx,rx):
        for col in range(ly,ry):
            board[row][col]=1

res=0
cntList=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            cnt=0
            res+=1
            DFS(i,j)
            if cnt==0:
                cnt=1
            cntList.append(cnt)

print(res)
cntList.sort()
for x in cntList:
    print(x,end=' ')