def solution(n):
    answer = 0
    l, r = 1, 1

    while l <= r:
        tot = 0
        for i in range(l, r+1):
            tot += i
        if tot == n:
            answer += 1
        if tot >= n:
            l += 1
        elif tot < n:
            r += 1

    return answer
