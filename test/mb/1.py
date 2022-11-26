def solution(flowers):
    answer = 0
    dp = [0 for _ in range(366)]

    for start, end in flowers:
        for i in range(start, end):
            if dp[i] == 0:
                dp[i] += 1
    
    answer = dp.count(1)


    return answer