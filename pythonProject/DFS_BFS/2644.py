#2664 촌수계산
import sys
def DFS(V,sum):
  ch[V]=1 #방문 표시
  if V==b:
    print(sum)
    sys.exit()
  else:
    for x in graph[V]:
      if ch[x]==0:
        DFS(x,sum+1)

n=int(input())
a,b=map(int,input().split()) #촌수 계산 두사람
m=int(input()) #부모자식간 관계 수
graph=[[]*n for _ in range(n+1)]
for _ in range(m):
  x,y=map(int,input().split()) #x가 부모
  graph[x].append(y) #x의 자녀엔 y가 있다.
  graph[y].append(x)

ch=[0]*(n+1)
DFS(a,0)
print(-1)