#10845 큐
from collections import deque
n=int(input()) #명령의 수
command=[]
for i in range(n):
    s=input().split()
    command.append(s)

Q=deque()
for x in command:
    if x[0]=='push':
        Q.append(x[1])
    elif x[0]=='pop':
        if len(Q)>0:
            print(Q.popleft())
        else:
            print(-1)
    elif x[0]=='size':
        print(len(Q))
    elif x[0]=='empty':
        if len(Q)>0:
            print(0)
        else:
            print(1)
    elif x[0]=='front':
        if len(Q)>0:
            print(Q[0])
        else:
            print(-1)
    elif x[0]=='back':
        if len(Q)>0:
            print(Q[-1])
        else:
            print(-1)