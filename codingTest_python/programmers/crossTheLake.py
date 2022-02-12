def solution(stones, k):
    answer = 0
    i = 0
    while True:
        idx = 0
        for i in range(len(stones)):
            if stones[idx] >= 1:
                stones[idx] -= 1
            else:
                while idx < len(stones):
                    if stones[idx] >= 1:
                        break
                    idx += 1
                if idx - i >= k:
                    return answer
            idx = i+1
        answer += 1

    return answers
