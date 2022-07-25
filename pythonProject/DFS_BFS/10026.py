#10026 적록색약
#색도 파라미터로 넘기기
#적록색약인 경우는 R을 G로 치환해서 한번 더 돌려주기
import sys
sys.setrecursionlimit(10000)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y,c): #마지막 파라미터 c는 색깔
    ch[x][y]=1 #방문 표시
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0:
            if c==board[xx][yy]: #색깔이 전에꺼랑 같으면
                DFS(xx,yy,board[xx][yy])

n=int(input())
board=[]
for _ in range(n):
    tmp=list(input())
    board.append(tmp)

resN=0 #적록색약 아님
ch=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ch[i][j]==0:
            resN+=1
            DFS(i,j,board[i][j])

resY=0 #적록색약 환자
ch=[[0]*n for _ in range(n)] #다시 초기화
for i in range(n):
    for j in range(n):
        if board[i][j]=='G':
            board[i][j]='R' #치환
for i in range(n):
    for j in range(n):
        if ch[i][j]==0:
            resY+=1
            DFS(i,j,board[i][j])


print(resN,resY, end=' ')