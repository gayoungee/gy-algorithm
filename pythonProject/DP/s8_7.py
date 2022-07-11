#알리바바와 40인의 도둑
#최단 거리 이동 => 오른쪽 or 아래쪽으로만 이동
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]

#초기화
dy[0][0]=board[0][0]
for i in range(1,n):
    dy[0][i]=dy[0][i-1]+board[0][i]
    dy[i][0]=dy[i-1][0]+board[i][0]

for i in range(1,n):
    for j in range(1,n):
        dy[i][j]=min(dy[i-1][j],dy[i][j-1])+board[i][j]

print(dy[n-1][n-1])
