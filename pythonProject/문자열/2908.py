#2908 상수
a,b=map(str,input().split())

ra="".join(reversed(a))
rb="".join(reversed(b))

if int(ra>=rb):
  print(ra)
else:
  print(rb)