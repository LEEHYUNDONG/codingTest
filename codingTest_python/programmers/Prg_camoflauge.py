def solution(clothes):
    answer = 1
    clothesDic = {}
    for i in clothes:
        if i[1] not in clothesDic.keys():
            clothesDic[i[1]] = []
            clothesDic[i[1]].append(i[0])
        else:
            clothesDic[i[1]].append(i[0])
    for i in clothesDic.keys():
        answer *= (len(clothesDic[i]) + 1)

    return answer - 1
