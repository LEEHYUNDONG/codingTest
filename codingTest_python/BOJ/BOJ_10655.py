import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
check = [list(map(int, input().split())) for _ in range(n)]
tot = 0
skip = 0

x, y = check[0][0], check[0][1]
for i in range(1, n):
    tot += abs(x-check[i][0]) + abs(y-check[i][1])
    x, y = check[i][0], check[i][1]

for i in range(1, n-1):
    prev = check[i-1]
    cur = check[i]
    nex = check[i+1]
    dist = abs(prev[0]-cur[0]) + abs(prev[1]-cur[1]) + \
        abs(cur[0]-nex[0]) + abs(cur[1]-nex[1])
    straight = abs(prev[0]-nex[0]) + abs(prev[1]-nex[1])
    skip = max(skip, dist - straight)

print(tot-skip)

# for i in range(1, n-1):
#     x, y = sx, sy
#     dist = 0
#     for j in range(1, n):
#         if check[i][0] == check[j][0] and check[i][1] == check[j][1]:
#             continue
#         dist += abs(x-check[j][0]) + abs(y-check[j][1])
#         x, y = check[j][0], check[j][1]
#     res = min(res, dist)
