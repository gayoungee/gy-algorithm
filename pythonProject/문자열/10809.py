s=input()
al=[-1]*26
for x in s:
    tmp=s.find(x)
    al[ord(x)-97]=tmp

for i in al:
    print(i,end=' ')
