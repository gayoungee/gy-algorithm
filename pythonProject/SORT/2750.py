n=int(input())
a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
a.sort()
for x in a:
    print(x)