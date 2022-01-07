import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 10000001
tmp = []
visited = [False] * n


def dfs(depth):
    if depth == n:
        global ans
        tot = 0
        for i in range(1, len(tmp)):
            if arr[tmp[i-1]][tmp[i]] == 0:
                return
            tot += arr[tmp[i-1]][tmp[i]]
        if arr[tmp[-1]][tmp[0]] == 0:
            return
        tot += arr[tmp[-1]][tmp[0]]
        ans = min(tot, ans)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        tmp.append(i)
        dfs(depth+1)
        tmp.pop()
        visited[i] = False


dfs(0)
print(ans)
