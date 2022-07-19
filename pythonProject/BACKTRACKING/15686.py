# 15686 치킨 배달
# 0 빈칸 / 1 집 / 2 치킨집
# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨거리: 모든 집의 치킨거리의 합

#1. 도시의 집과 치킨집 좌표를 획득
#2. 치킨집 중에 m개를 선택하며 치킨거리를 다 구해본다 (백트래킹)
#3. 가장 치킨 거리가 좋았던 치킨집들의 조합의 '도시의 치킨거리'를 구함

from itertools import combinations
n,m=map(int,input().split())
board=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    board.append(tmp)
home=[]
store=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            home.append([i,j])
        elif board[i][j]==2:
            store.append([i,j])

res=2147000000 #최종 선택된 도시의 치킨 거리
for ss in combinations(store,m): #store set 조합
    tmp=0 #도시의 치킨거리
    for h in home:
        cl=2147000000
        for i in range(m): #한개의 집과 골라진 m개의 치킨집중에 가장 가까운 거리
            cl=min(cl,abs(h[0]-ss[i][0])+abs(h[1]-ss[i][1]))
        tmp+=cl
    res=min(res,tmp)

print(res)




