import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sack = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(k+1)]

for i in range(n):
    print(dp)
    for j in range(k, 1, -1):  # j는 무게이다.
        if sack[i][0] <= j:  # 무게가 더 가벼울때
            dp[j] = max(dp[j], dp[j - sack[i][0]]+sack[i][1])
    print(dp)
print(dp[k])
