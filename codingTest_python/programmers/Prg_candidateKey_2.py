from itertools import combinations


def findDup(ans, comb):
    cnt = 0
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            if ans[i][j] in comb:
                cnt += 1
        if cnt == len(ans[i]):
            return True
    return False


def solution(relation):
    answer = 0
    ans = []
    for k in range(1, len(relation[0])+1):
        for i in combinations([i for i in range(len(relation[0]))], k):
            if findDup(ans, i):
                continue
            else:
                tmp = {}
                t = ""
                for j in range(len(relation)):
                    t = ""
                    for q in i:
                        t += relation[j][q]
                    if t not in tmp.keys():
                        tmp[t] = 1
                    else:
                        tmp[t] += 1
                # uniqueness
                if len(tmp) == len(relation):
                    ans.append(list(i))
                    print(ans)
                    answer += 1
    return answer
