n = int(input())
dp = [0] * (n+1)
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)
print(dp[n])
'''
숫자 1이 될 때 까지 연산의 최소 횟수이기 때문에 1로부터 26을 구해나가야 한다.

'''
