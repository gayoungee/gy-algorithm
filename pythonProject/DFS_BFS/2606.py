def DFS(V):
  global res
  ch[V]=1
  for i in graph[V]:
    if ch[i]==0:
      res+=1
      DFS(i)

n=int(input()) #컴퓨터의 수
m=int(input()) #직접 연결되어 있는 컴퓨터 쌍의 수
graph=[[]*n for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

res=0
ch=[0]*(n+1)
DFS(1)
print(res)