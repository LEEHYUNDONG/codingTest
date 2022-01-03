from itertools import combinations


def solution(relation):
    answer = 0
    r = len(relation)
    c = len(relation[0])

    comb = []
    for i in range(1, c+1):
        comb.extend(combinations(range(c), i))

    unique = []
    for i in comb:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == r:
            flag = True
            for x in unique:
                if set(x).issubset(set(i)):
                    flag = False
                    break
            if flag:
                unique.append(i)

    return len(unique)
