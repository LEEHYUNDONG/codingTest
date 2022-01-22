def solution(board):
    rows, cols = len(board), len(board[0])
    answer = 0
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            dp[i][j] = board[i-1][j-1]

    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

            answer = max(answer, dp[i][j])

    return answer**2
