#가장 높은 탑 쌓기
n=int(input()) #벽돌의 갯수
dy=[0]*(n+1)
rock=list()
for i in range(n):
    s,h,w=map(int,input().split()) #벽돌의 정보
    rock.append((s,h,w))

#벽돌을 쌓아보자
#일단 밑면의 넓이 순서대로 정렬을 함
rock.sort(reverse=True)
dy[0]=rock[0][1] #0번째 벽돌의 높이(h)
res=rock[0][1]

for i in range(1,n):
    maxHeight=0
    for j in range(i-1,-1,-1):
        if rock[j][2]>rock[i][2] and dy[j]>maxHeight:
            maxHeight=dy[j]
    dy[i]=maxHeight+rock[i][1]
    res=max(res,dy[i])

print(res)
