import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
check = [list(map(int, input().split())) for _ in range(n)]
res = 0
x, y = check[0][0], check[0][1]
dist = int(1e9)

for i in range(1, n):
    res += abs(x-check[i][0]) + abs(y-check[i][1])
    x, y = check[i][0], check[i][1]

for i in range(1, n-1):
    
print(res, dist)

# for i in range(1, n-1):
#     x, y = sx, sy
#     dist = 0
#     for j in range(1, n):
#         if check[i][0] == check[j][0] and check[i][1] == check[j][1]:
#             continue
#         dist += abs(x-check[j][0]) + abs(y-check[j][1])
#         x, y = check[j][0], check[j][1]
#     res = min(res, dist)
