#1316 그룹 단어 체커
def makeIdxDic(word): #그룹단어 체크용 함수
    sw=sorted(set(word))
    dic={}
    for i in range(len(sw)):
        dic[sw[i]]=i
    return dic

n=int(input())
word=[]
for i in range(n):
    tmp=input()
    word.append(tmp)

res=0
for x in word:
    ddic=makeIdxDic(x)
    ch=[]
    ch.append(ddic[x[0]]) #처음껀 그냥 넣어 두고
    for j in range(1,len(x)):
        if ch[-1]!=ddic[x[j]]:
            ch.append(ddic[x[j]])
    if len(ddic)==len(ch):
        res+=1
print(res)