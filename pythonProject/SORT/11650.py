#11650 좌표 정렬하기

n=int(input()) #점의 개수
board=list()
for i in range(n):
    x,y=map(int,input().split())
    board.append((x,y))
board.sort()

for i in range(n):
    print(board[i][0],board[i][1])