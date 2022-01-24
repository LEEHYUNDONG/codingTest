from itertools import combinations


def solution(arr):
    answer = 1
    arr.sort(reverse=True)
    res = set()
    for i in arr:
        for j in range(2, i+1):
            if i % j == 0:
                res.add(j)

    for k in range(1, len(res)):
        for i in combinations(list(res), k+1):
            answer = 1
            for j in i:
                answer *= j
            flag = True
            for j in arr:
                if answer % j != 0:
                    flag = False
                    break
            if flag:
                return answer
