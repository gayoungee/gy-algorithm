#1654 랜선 자르기
# 같은 길이의 랜선으로, n개를 만들고 싶다
# n개의 랜선 크기의 범위는 1보다 크고 입력된 k개의 랜선들 중 가장 긴거보다 작다.
# 이렇게 범위 안에 들어간 답을 구하고 싶으면 => 이분검색
k,n=map(int,input().split())
a=[]
for _ in range(k):
    tmp=int(input())
    a.append(tmp)
maxLen=max(a)
lt=1
rt=maxLen
res=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for i in range(k):
        cnt+=a[i]//mid
    if cnt>=n:
        res=mid
        lt=mid+1 # 더 좋은 답을 찾아나감
    else:
        rt=mid-1
print(res)
