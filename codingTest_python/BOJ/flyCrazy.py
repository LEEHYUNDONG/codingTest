import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dp = [[-int(1e9)]*(m+1) for _ in range(n+1)] # 상승 비행
dp2 = [[-int(1e9)]*(m+1) for _ in range(n+1)] 
dp[n-1][0] = graph[n-1][0]
dp2[n-1][m-1] = graph[n-1][m-1]

# 상승 비행
for i in range(n-1, -1, -1):
    for j in range(m):
        if i == n-1 and j == 0:
            continue
        dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + graph[i][j]
        


# 하강 비행

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            continue
        dp2[i][j] = max(dp2[i+1][j], dp2[i][j+1]) + graph[i][j] # 왼쪽 위
        
ans = -int(1e9)
for i in range(n+1):
    for j in range(m+1):
        ans = max(ans, dp[i][j]+dp2[i][j])

print(ans)