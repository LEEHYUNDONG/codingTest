import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [[0]*(n+1)]

for _ in range(n):
    dp.append([0]+list(map(int, input().split())))

test = [list(map(int, input().split())) for _ in range(m)]

# 행별로 덧셈을 계산 하기
for i in range(1, n+1):
    for j in range(1, n):
        dp[i][j+1] += dp[i][j]

# 열별로 계산
for j in range(1, n+1):
    for i in range(1, n):
        dp[i+1][j] += dp[i][j]


for x1, y1, x2, y2 in test:
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])