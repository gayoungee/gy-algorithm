n=int(input())
s=int(input())
sum=0
while True:
  if s<=0:
    break
  sum+=s%10
  s=s//10

print(sum)