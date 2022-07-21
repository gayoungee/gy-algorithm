#11724 연결 요소의 개수
import sys
sys.setrecursionlimit(10001)
def DFS(V):
    for i in range(1,n+1):
        if board[V][i]==1 and ch[i]==0:
            ch[i]=1 #방문 표시
            DFS(i)

n,m=map(int,input().split())
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    board[u][v]=1
    board[v][u]=1

ch=[0]*(n+1)
res=0

for i in range(1,n+1):
    if ch[i]==0:
        ch[i]=1
        DFS(i)
        res+=1

print(res)