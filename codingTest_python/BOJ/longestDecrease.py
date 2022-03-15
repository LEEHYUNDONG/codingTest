import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))