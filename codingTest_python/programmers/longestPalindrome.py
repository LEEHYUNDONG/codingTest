def solution(s):
    answer = 1
    n = len(s)

    for i in range(n):
        for j in range(i + 2, n + 1):
            tmp = s[i:j]
            # print(tmp)
            if len(tmp) < answer:
                continue
            if tmp == tmp[::-1]:
                answer = max(answer, j - i)

    return answer
