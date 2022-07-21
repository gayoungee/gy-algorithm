from collections import deque
def DFS(V):
    print(V,end=' ')
    for i in range(1,n+1):
        if board[V][i]==1 and chDfs[i]==0:
            chDfs[i]=1
            DFS(i)

def BFS(V):
    Q=deque()
    Q.append(V)
    while Q:
        tmp=Q.popleft()
        print(tmp,end=' ')
        for i in range(1,n+1):
            if board[tmp][i]==1 and chBfs[i]==0:
                chBfs[i]=1
                Q.append(i)

n,m,v=map(int,input().split())
board=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    board[a][b]=1
    board[b][a]=1

chDfs=[0]*(n+1)
chBfs=[0]*(n+1)

chDfs[v]=1
DFS(v)
print()
chBfs[v]=1
BFS(v)