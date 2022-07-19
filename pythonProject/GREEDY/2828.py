#2828 사과 담기 게임
n,m=map(int, input().split())
j=int(input())
apple=[]
for _ in range(j):
    tmp=int(input())
    apple.append(tmp)

lp=1
rp=m
res=0

for i in range(j):
    if apple[i]>rp and rp+(apple[i]-rp)<n+1:
        cha= apple[i]-rp
        lp=lp+cha
        rp=rp+cha
        res+=cha
    elif apple[i]<lp and lp-(lp-apple[i])>0:
        cha= lp-apple[i]
        lp=lp-cha
        rp=rp-cha
        res+=cha
print(res)