n = int(input())
a = []
stack = []

for i in range(n):
    tmp = input().split()
    a.append(tmp)

for x in a:
    if x[0] == 'push':
        stack.append(x[1])
    elif x[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
    elif x[0] == 'size':
        print(len(stack))
    elif x[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif x[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)