#15649 n과 m
def DFS(L):
    if L==m:
        for i in range(m):
            print(res[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

n,m=map(int,input().split())
res=[0]*m
ch=[0]*(n+1)
DFS(0)