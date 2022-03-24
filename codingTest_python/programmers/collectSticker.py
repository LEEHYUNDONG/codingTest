def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp = [0]*n
    dp[0] = sticker[0]

    for i in range(1, n-1):
        if i == 1:
            dp[i] = max(sticker[i], dp[i-1])
        else:
            dp[i] = max(sticker[i]+dp[i-2], dp[i-1])

    answer = max(dp)

    dp = [0]*n
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(sticker[i]+dp[i-2], dp[i-1])

    answer = max(max(dp), answer)

    return answer
