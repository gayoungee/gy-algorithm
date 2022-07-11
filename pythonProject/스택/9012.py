n = int(input())
a = []
for i in range(n):
    tmp = input()
    a.append(tmp)

for x in a:
    l = list(x)
    stack = []

    for e in l:
        if e == ')' and len(stack) > 0:
            stack.pop()
        elif e == ')' and len(stack) < 0:
            print('NO')
            break
        else:
            stack.append(e)

    if len(stack) > 0:
        print('NO')
    else:
        print("YES")

