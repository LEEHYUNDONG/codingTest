import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
t = int(input())
dp = [[0]*n for _ in range(n)]

def checkPal(arr, start, end):
    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

for i in range(n):
    dp[i][i] = 1
    for j in range(i+1, n):
        if checkPal(arr, i, j):
            dp[i][j] = 1


for _ in range(t):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if dp[start][end]:
        print(1)

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# t = int(input())
# dp = [[-1]*n for _ in range(n)]

# def checkPal(arr, start, end):
#     if start == end: # 홀의 경우
#         return 1
#     elif start == end-1: # 짝의 경우
#         if arr[start] == arr[end]:
#             return 1
#         else:
#             return 0
#     if dp[start][end] != -1: # 이미계산된 적이 있다면 return
#         return dp[start][end]
    
#     if arr[start] == arr[end]: # 같으면 메모이제이션
#         dp[start][end] = checkPal(arr, start+1, end-1)
#     else:
#         dp[start][end] = 0
#     return dp[start][end]


# for _ in range(t):
#     start, end = map(int, input().split())
#     print(checkPal(arr, start-1, end-1))