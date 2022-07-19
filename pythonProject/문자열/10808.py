#10808 알파벳 개수
s=input()
alpha=[0]*26
ss=sorted(set(s))
for x in ss:
    cnt=s.count(x)
    alpha[ord(x)-97]=cnt
for i in alpha:
    print(i,end=' ')