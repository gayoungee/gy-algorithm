# 1764 듣보잡
#문제의 핵심은 교집합 찾기!
n,m=map(int,input().split())
d=[] #듣도
b=[] #보도
for _ in range(n):
    tmp=input()
    d.append(tmp)
for _ in range(m):
    tmp=input()
    b.append(tmp)

db=list(set(d) & set(b)) # 집합 연산자

print(len(db))
for x in sorted(db):
    print(x)