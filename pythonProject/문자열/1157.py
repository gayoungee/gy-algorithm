#1157 단어 공부
s=input().upper()
setS=set(s)
res=0
resC=''
for x in setS:
  cnt=s.count(x)
  if cnt>res:
    res=cnt
    resC=x
  elif cnt==res:
    resC+=x

if len(resC)>1:
  print('?')
else:
  print(resC)5