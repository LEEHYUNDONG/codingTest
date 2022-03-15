import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp1 = [1]*n 
dp2 = [1]*n
tmp = [0]*n
        

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[j]+1, dp1[i])


for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[j]+1, dp2[i])
    tmp[i] =  dp2[i]+dp1[i] -1

# print(dp1)
# print(dp2)
print(max(tmp))