from collections import deque
#9205 맥주 마시면서 걸어가기
t=int(input())
m=20 #상근이의 맥주 개수
#50미터를 가기 전 맥주를 마셔야 한다

def BFS():
  Q=deque()
  Q.append((sx,sy))
  while Q:
    tmp=Q.popleft()
    if abs(tmp[0]-rx)+abs(tmp[1]-ry)<=1000:
      print("happy")
      return
    for i in range(n):
      if ch[i]==0:
        xx,yy=cboard[i]
        if abs(xx-rx)+abs(yy-ry)<=1000:
          ch[i]=1
          Q.append((xx,yy))
    print("sad")
    return

cboard=[]
for i in range(t):
  n=int(input()) #편의점의 개수
  sx,sy=map(int,input().split()) #상근이집
  for j in range(n):
    cx,cy=map(int,input().split()) #편의점 좌표
    cboard.append([cx,cy])
  rx,ry=map(int,input().split()) #락페 좌표
  ch=[[0] for _ in range(n+1)]
  BFS()