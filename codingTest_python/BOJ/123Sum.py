import sys
input = sys.stdin.readline

t = int(input())
test = []
for _ in range(t):
    test.append(int(input()))

dp = [0 for _ in range(max(test)+1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max(test)+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

for i in test:
    print(dp[i])