#11866 요세푸스 문제 0
from collections import deque
n,k=map(int,input().split())

Q=deque(range(1,n+1))

res=[]
#k번째 사람 제거 진행
while Q:
    for _ in range(k-1):
        tmp=Q.popleft()
        Q.append(tmp)
    remove=Q.popleft() # k번째 사람 제거
    res.append(remove)

print('<',end='')
for i in range(len(res)-1):
    print("%d, " %res[i], end='')
print(res[-1],end='')
print('>',end='')
