#2910 빈도 정렬
#python은 기본적으로 안정정렬
n,c=map(int,input().split())
message=list(map(int,input().split()))
dic={}
for i in range(n):
    if message[i] in dic:
        dic[message[i]]+=1
    else:
        dic[message[i]]=1

dic=sorted(dic.items(),key=lambda x:x[1], reverse=True)

for key,val in dic:
    for i in range(val):
        print(key, end=' ')