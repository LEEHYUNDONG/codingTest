from itertools import combinations


def solution(n, info):
    answer = []
    score = []  # 어피치, 라이언 점수
    res = 0
    idx = 0
    for k in range(1, n):
        for i in combinations([i for i in range(11)], k):
            ans = [0 for _ in range(11)]
            for j in i:
                ans[j] = info[j]+1
            for j in range(10, -1, -1):
                if j not in i and sum(ans) < n and info[j] > 1 and ans[j] == 0:
                    ans[j] = info[j]-1
                if sum(ans) == n:
                    apeach, lion = 0, 0
                    for r in range(11):
                        if info[r] == 0 and ans[r] == 0:
                            continue
                        elif info[r] >= ans[r]:
                            apeach += 10-r
                        else:
                            lion += 10-r
                    if apeach < lion:
                        if sum(ans) == n and apeach < lion:
                            score.append([idx, lion-apeach])
                            answer.append(ans)
                            idx += 1

    score.sort(key=lambda x: x[1], reverse=True)
    if len(score) >= 1:
        idx = 0
        maxV = score[0][1]
        for i in score:
            if i[1] == maxV:
                idx = i[0]
                continue
            else:
                break
        return answer[idx]
    else:
        return [-1]
