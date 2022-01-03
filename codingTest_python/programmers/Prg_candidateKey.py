from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합
    comb = []
    for i in range(1, col+1):
        comb.extend(combinations(range(col), i))

    # unique
    unique = []
    for i in comb:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        if len(set(tmp)) == row:    # 유일성
            flag = True
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    flag = False
                    break
            if flag:
                unique.append(i)

    return len(unique)
