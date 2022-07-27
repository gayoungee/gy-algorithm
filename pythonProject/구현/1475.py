#1475 방 번호
import math
n=list(input()) #다솜이 방번호 (은진이 옆집)
cnt=[0]*10 #0~9까지
for i in range(len(n)):
    idx=int(n[i])
    cnt[idx]+=1

#0~5 7~8
maxIdx=0
for i in range(0,6):
    if cnt[i]>cnt[maxIdx]:
        maxIdx=i
for i in range(7,9):
    if cnt[i]>cnt[maxIdx]:
        maxIdx=i

maxCnt=cnt[maxIdx]
maxS=max(cnt[6],cnt[9])

if maxCnt>=maxS:
    print(maxCnt)
else:
    fCnt=(cnt[6]+cnt[9])/2
    if maxCnt>fCnt:
        print(maxCnt)
    else:
        print(math.ceil(fCnt))



