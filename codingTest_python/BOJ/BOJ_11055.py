import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += seq[i]


print(max(dp))
