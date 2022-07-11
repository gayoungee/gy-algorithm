#네트워크 선자르기 (Top-down, 재귀)
def DFS(V):
    if dy[V]>0: #가지 cut
        return dy[V]
    if V==1 or V==2:
        return V
    else:
        dy[V]=DFS(V-1)+DFS(V-2) #메모이제이션
        return dy[V]

n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
print(DFS(n))