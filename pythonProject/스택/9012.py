#9012 괄호
#stack
def solution(s):
    stack=[]
    for x in s:
        if x=='(':
            stack.append(x)
        elif x==')':
            if len(stack)>0:
                stack.pop()
            else:
                return 0
    if len(stack)>0:
        return 0
    else:
        return 1

res=[]
t=int(input())
for i in range(t):
    a=list(input())
    tmp=solution(a)
    if tmp==1:
        res.append("YES")
    else:
        res.append("NO")
for x in res:
    print(x)
