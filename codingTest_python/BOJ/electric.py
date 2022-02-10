import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
dp = [1]*101
lines.sort()

for i in range(n):
    for j in range(i):
        if lines[i][1] >lines[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(n - max(dp))