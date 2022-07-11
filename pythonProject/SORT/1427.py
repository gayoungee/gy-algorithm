#1427 소트인사이드
n=int(input())

#자리수를 내림차순으로 정리..
count=[0]*10 #0~9 까지 몇번 나오는지 카운트
while True:
    if n<10:
        count[n]+=1
        break
    else:
        tmp=n%10
        count[tmp]+=1
        n=n//10

res=''
for i in range(9,-1,-1):
    res+=str(i)*count[i]
print(res)