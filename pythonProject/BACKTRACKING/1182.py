#1182 부분수열의 합
def DFS(i,sum):
    global cnt
    if i==n:
        return
    sum+=a[i]
    if sum==s:
        cnt+=1
    DFS(i+1,sum) #해당 인덱스의 수 선택했다
    DFS(i+1,sum-a[i]) #해당 인덱스의 수 선택 안했다

n,s=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
DFS(0,0)
print(cnt)