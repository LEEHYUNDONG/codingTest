def solution(gems):
    answer = [1, 100000]
    size = len(set(gems))
    l, r = 0, 0
    while l <= r:
        tmp = []
        for i in range(l, r):
            tmp.append(gems[i])
        if size == len(set(tmp)) and (answer[1] - answer[0]) > (r - l):
            answer = [l+1, r]
        if size <= len(tmp):
            l += 1
        elif size > len(tmp) and r < len(gems):
            r += 1
        
    return answer