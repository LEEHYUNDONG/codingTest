import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N)]
arr = list(map(int, input().split()))
ans = 0

for i in range(N):
    dp[i] = arr[i]
    dp[i] = max(dp[i-1]+arr[i], dp[i])
    
print(max(dp))