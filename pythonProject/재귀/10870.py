def pibo(x):
  res=0
  if x==0:
    res=0
  elif x==1:
    res=1
  else:
    res=pibo(x-2)+pibo(x-1)
  return res

n=int(input())
print(pibo(n))