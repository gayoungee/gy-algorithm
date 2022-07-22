#17219 비밀번호 찾기
#딕셔너리 활용
n,m=map(int,input().split())
dic={}
fd=[]
for i in range(n):
    a,p=list(input().split())
    dic[a]=p
for i in range(m):
    f=input()
    fd.append(f)
for x in fd:
    if x in dic:
        print(dic[x])