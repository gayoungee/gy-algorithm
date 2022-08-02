#완전탐색_lv2_카펫
def solution(brown, yellow):
    answer = []
    area=brown+yellow #두개 합친게 넓이
    for h in range(3,(area//3)+1):
        if area%h==0:
            w=area//h
            if (w-2)*(h-2)==yellow and w>=h:
                answer.append([w,h])
    return answer[0]