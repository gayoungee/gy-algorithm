# 2468 안전영역
import sys

sys.setrecursionlimit(100000)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > h and ch[xx][yy] == 0:
            DFS(xx, yy, h)


n = int(input())
board = list()

# 최대 높이를 먼저 파악해야 함
maxHeight = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    if max(tmp) > maxHeight:
        maxHeight = max(tmp)
    board.append(tmp)

res = 0
for h in range(0, maxHeight + 1):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and board[i][j] > h:
                cnt += 1
                DFS(i, j, h)
    if cnt > res:
        res = cnt

print(res)