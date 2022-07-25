# 2751 수 정렬하기 2
n=int(input())
a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
a.sort()
for x in a:
    print(x)