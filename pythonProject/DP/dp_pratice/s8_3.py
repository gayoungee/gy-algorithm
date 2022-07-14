#계단 오르기
def DFS(V):
    if dy[V]>0:
        return dy[V]
    if V==1 or V==2:
        return dy[V]
    else:
        dy[V]=DFS(V-1)+DFS(V-2)
        return dy[V]

n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
print(DFS(n))

