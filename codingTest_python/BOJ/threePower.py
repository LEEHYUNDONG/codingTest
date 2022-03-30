import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(3)
    exit()

dp[1] = 1
dp[2] = 3
cnt = 2
tmp = 2**cnt
for i in range(3, n+1):
    if tmp == i:
        dp[i] = 3*dp[tmp//2]
        cnt += 1
        tmp = 2**(cnt)
    else:
        dp[i] = dp[tmp//2] + dp[(i%(tmp//2))]

print(dp[n])