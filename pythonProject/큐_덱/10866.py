#10866 덱
from collections import deque
n=int(input()) #명령의 수
command=[]
for i in range(n):
    com=input().split()
    command.append(com)

Q=deque()
for i in range(n):
    if command[i][0]=='push_front':
        Q.appendleft(command[i][1])
    elif command[i][0]=='push_back':
        Q.append(command[i][1])
    elif command[i][0]=='pop_front':
        if len(Q)>0:
            tmp=Q.popleft()
            print(tmp)
        else:
            print(-1)
    elif command[i][0]=='pop_back':
        if len(Q)>0:
            print(Q.pop())
        else:
            print(-1)
    elif command[i][0]=='size':
        print(len(Q))
    elif command[i][0]=='empty':
        if len(Q)>0:
            print(0)
        else:
            print(1)
    elif command[i][0]=='front':
        if len(Q)>0:
            print(Q[0])
        else:
            print(-1)
    elif command[i][0]=='back':
        if len(Q)>0:
            print(Q[-1])
        else:
            print(-1)
