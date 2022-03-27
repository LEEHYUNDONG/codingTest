import sys
n, k = map(int, input().split())

arr = list(map(int, input().split()))
dp = [0]*n

dp[0] = 1

for i in range(n):
    for j in range(i+1, n):
        if (j - i)*(1+abs(arr[i]-arr[j])) <= k and dp[i] != 0:
            dp[j] += 1
    

if dp[n-1] == 0:
    print('NO')
else:
    print('YES')
