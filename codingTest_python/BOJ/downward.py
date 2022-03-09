import sys
import copy
input = sys.stdin.readline

n = int(input())
tmp = [list(map(int, input().split())) for _ in range(n)]
ans = [[0, 0, 0], [0, 0, 0]]
answer =  []

ans[0][0] = tmp[0][0]
ans[0][1] = tmp[0][1]
ans[0][2] = tmp[0][2]

for i in range(1, n):
    ans[1][0] = max(ans[0][0], ans[0][1]) + tmp[i][0]
    ans[1][1] = max(max(ans[0][0], ans[0][1]), ans[0][2]) + tmp[i][1]
    ans[1][2] = max(ans[0][1], ans[0][2]) + tmp[i][2]

    ans[0][0], ans[0][1], ans[0][2] = ans[1][0], ans[1][1], ans[1][2]


answer.append(max(ans[0]))

ans[0][0] = tmp[0][0]
ans[0][1] = tmp[0][1]
ans[0][2] = tmp[0][2]

for i in range(1, n):
    ans[1][0] = min(ans[0][0], ans[0][1]) + tmp[i][0]
    ans[1][1] = min(min(ans[0][0], ans[0][1]), ans[0][2]) + tmp[i][1]
    ans[1][2] = min(ans[0][1], ans[0][2]) + tmp[i][2]

    ans[0][0], ans[0][1], ans[0][2] = ans[1][0], ans[1][1], ans[1][2]

answer.append(min(ans[0]))

print(*answer)