# n, m = map(int, input().split())
# # money = [int(input()) for _ in range(n)]
# money = []
# dp = [10001] * 100001
# dp[0] = 0

# for _ in range(n):
#     tmp = int(input())
#     money.append(tmp)
#     dp[tmp] = 1

# for i in range(min(money), m+1):
#     for j in money:
#         if i % j == 0:
#             dp[i] = min(dp[i], dp[i-j]+1)

# print(dp[:m+1])
# print(-1) if dp[n] == 10001 else print(dp[n])

n, m = map(int, input().split())
# money = [int(input()) for _ in range(n)]
money = []
dp = [10001] * 100001
dp[0] = 0
for _ in range((n)):
    money.append(int(input()))

for i in range(n):  # 가지고 있는 동전의 개수만큼 찾는다.
    for j in range(money[i], m+1):  # 동전의 개수의 배수들을 전부 원래 동전 개수 + 1
        dp[j] = min(dp[j], dp[j-money[i]]+1)

print(-1) if dp[m] == 10001 else print(dp[m])
