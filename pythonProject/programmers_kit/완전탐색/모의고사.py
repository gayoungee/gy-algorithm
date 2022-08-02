def solution(answers):
    answer = []
    size = len(answers)  # 문제의 갯수
    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for idx, x in enumerate(answers):
        if x == s_1[idx % len(s_1)]:
            cnt[0] += 1
        if x == s_2[idx % len(s_2)]:
            cnt[1] += 1
        if x == s_3[idx % len(s_3)]:
            cnt[2] += 1

    for idx, c in enumerate(cnt):
        if c == max(cnt):
            answer.append(idx + 1)

    return answer