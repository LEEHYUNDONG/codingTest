def solution(A, B):
    answer = 0
    B.sort(reverse=True)
    A.sort()

    for a, b in zip(A, B):
        answer += a*b

    return answer
