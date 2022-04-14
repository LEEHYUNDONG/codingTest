import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    coin = list(map(int, input().split()))
    money = int(input())
    dp = [0 for i in range(money+1)]
    dp[0] = 1
    for j in coin:
        for i in range(j, money+1):
            dp[i] += dp[i-j]

    print(dp[money])
