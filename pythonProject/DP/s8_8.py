#알리바바와 40인의 도둑 (top-down 방식)
def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    if x==0 and y==0:
        return board[0][0]
    else:
        if y==0:
            dy[x][y]=DFS(x-1,y)+board[x][y] #위로만 올라감
        elif x==0:
            dy[x][y]=DFS(x,y-1)+board[x][y] #왼쪽으로
        else:
            dy[x][y]=min(DFS(x-1,y)+board[x][y],DFS(x,y-1)+board[x][y])
        return dy[x][y]
n=int(input())
board=list()
board=[list(map(int,input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)] #메모이제이션
print(DFS(n-1,n-1))