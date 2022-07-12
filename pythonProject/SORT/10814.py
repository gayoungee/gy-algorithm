# 10814 나이순 정렬
n=int(input())
p=[]
for i in range(n):
    a,b=input().split()
    p.append([int(a),b,i])
p.sort(key=lambda x:(x[0],x[2]))

for x in p:
    print(x[0],x[1])