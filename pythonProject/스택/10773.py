k=int(input())
stack=[]
for i in range(k):
  tmp=int(input())
  if tmp==0:
    stack.pop()
  else:
    stack.append(tmp)
res=sum(stack)
print(res)