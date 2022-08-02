# 완전탐색 : 소수 찾기
from itertools import permutations
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True

s=input()
a=list(s)
size=len(a)
permu=[]
cnt=[]
for i in range(1,size+1):
    permu+=list(permutations(a,i))

perjoin=[int(("").join(x)) for x in permu]

for x in perjoin:
    if x<2:
        continue
    res=isPrime(int(x))
    if res:
        cnt.append(x)

print(len(set(cnt)))