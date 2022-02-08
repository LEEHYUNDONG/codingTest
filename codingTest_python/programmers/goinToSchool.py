def solution(m, n, puddles):
    answer = 0
    graph = [[0]*n for _ in range(m)]
    dp = [[0]*n for _ in range(m)]

    for x, y in puddles:
        graph[x-1][y-1] = -1

    for i in range(n):
        if graph[0][i] != -1:
            dp[0][i] = 1
        else:
            break

    for i in range(1, m):
        if graph[i][0] != -1:
            dp[i][0] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if graph[i][j] != -1:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[m-1][n-1]
