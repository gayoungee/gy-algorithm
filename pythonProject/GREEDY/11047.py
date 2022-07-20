#11047 동전 0
n,k=map(int,input().split())
coins=[]
for _ in range(n):
    tmp=int(input())
    coins.append(tmp)

cnt=0
for i in range(n-1,-1,-1):
    if k==0:
        break
    if coins[i]>k:
        continue
    cnt+=k//coins[i]
    k=k%coins[i]

print(cnt)