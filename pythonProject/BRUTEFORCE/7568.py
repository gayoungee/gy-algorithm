#7568 덩치
n=int(input())
student=[]
for i in range(n):
    w,h=map(int,input().split())
    student.append((w,h))

res=list()
for i in range(n):
    cnt=0
    for j in range(i-1,-1,-1): #앞부분 조사
        if student[j][0]>student[i][0] and student[j][1]>student[i][1]:
            cnt+=1
    for j in range(i+1,n): #뒷부분 조사
        if student[j][0]>student[i][0] and student[j][1]>student[i][1]:
            cnt+=1
    res.append(cnt+1)

for x in res:
    print(x,end=' ')