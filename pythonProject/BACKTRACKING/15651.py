def DFS(L):
    if L==m:
        for i in range(m):
            print(res[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)

n,m=map(int,input().split())
res=[0]*m
DFS(0)