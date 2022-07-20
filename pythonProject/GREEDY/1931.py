#1931 회의실 배정
n=int(input())
info=[]
for i in range(n):
    s,e=map(int,input().split())
    info.append([s,e])

#1. start 시간 기준으로 정렬
info=sorted(info,key=lambda x:x[0])

#2. start와 end 시간이 같을수도 있으므로 end 시간 기준 한번 더 정렬
info=sorted(info,key=lambda x:x[1])

res=0
lastTime=0

for s,e in info:
    if s>=lastTime:
        res+=1
        lastTime=e

print(res)