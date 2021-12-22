# RGB 거리
import sys
sys.setrecursionlimit(100000)
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
res = 0
ans = []
color = [-1]


def backtrack(i, c, index):
    global res
    if i == n:
        res = min(res, c)
        ans.append(res)
        return
    for j in range(3):
        res += cost[i][j]
        backtrack(i+1, res, j)
        res -= cost[i][j]


backtrack(0, 0, -1)
print(ans)
