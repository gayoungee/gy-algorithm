#11478 서로 다른 부분 문자열 개수
s=input()
size=len(s)

res=[]
for i in range(size+1):
    for j in range(i+1,size+1):
        res.append(s[i:j])

sres=set(res)
print(len(sres))
