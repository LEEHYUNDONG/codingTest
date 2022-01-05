import sys
input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
ans = -1000
day = 0


def dfs(idx, tot):
    global ans
    if idx == n:
        ans = max(tot, ans)
        return

    if schedule[idx][0] + idx <= n:
        dfs(idx+schedule[idx][0], tot + schedule[idx][1])

    dfs(idx+1, tot)


dfs(0, 0)
print(ans)
