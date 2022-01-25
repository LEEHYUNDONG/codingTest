from itertools import combinations


def solution(n, info):
    answer = []
    score = []  # 어피치, 라이언 점수
    res = 0
    idx = 0
    for k in range(1, n):
        for i in combinations([i for i in range(11)], k):
            ans = [0 for _ in range(11)]
            arrow = n
            for j in range(len(info)):
                if j in i:
                    ans[j] = info[j]+1

            if sum(ans) == n:
                apeach, lion = 0, 0
                for j in range(11):
                    if info[j] == 0 and ans[j] == 0:
                        continue
                    elif info[j] >= ans[j]:
                        apeach += 10-j
                    else:
                        lion += 10-j
                if apeach < lion:
                    score.append([idx, lion-apeach])
                    answer.append(ans)
                    idx += 1

    score.sort(key=lambda x: x[1], reverse=True)
    if len(score) >= 1:
        return answer[score[0][0]]
    else:
        return [-1]
