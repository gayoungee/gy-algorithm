#2661 좋은 수열
#1,2,3을 차례대로 뒤에 붙이면서, 좋은수열인지 확인한다.
import sys
def checkGood(x):
    for i in range(1,len(x)//2+1):
        if x[-i:]==x[-(i*2):-i]:
            return False
    else:
        return True

def backTracking(x):
    global n
    if len(x)==n:
        print(x)
        sys.exit()
    for i in '123':
        if checkGood(x+str(i)):
            backTracking(x+str(i))
    return

n=int(input())
backTracking('1')