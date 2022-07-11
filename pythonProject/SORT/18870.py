#18870 좌표 압축
n=int(input())
a=list(map(int,input().split()))
sa=sorted(set(a)) # set을 이용한 중복 제거 및 정렬

dic={}
for i in range(len(sa)):
    dic[sa[i]]=i #인덱스 사전 만들기
for x in a:
    print(dic[x],end=' ')