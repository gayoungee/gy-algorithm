#11651 좌표 정렬하기2

n=int(input()) #점의 개수
board=list()
for i in range(n):
    x,y=map(int,input().split())
    board.append((x,y))
board.sort(key=lambda k:(k[1],k[0]))

for i in range(n):
    print(board[i][0],board[i][1])