from collections import deque
n=int(input())

Q=deque(range(1,n+1))

while len(Q)>1:
  Q.popleft()
  tmp=Q.popleft()
  Q.append(tmp)

print(Q[0])