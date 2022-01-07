import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = -1000
tmp = []
visited = [False] * n


def dfs(depth):
    if depth == n:
        global ans
        tot = 0
        for i in range(1, len(tmp)):
            tot += abs(arr[tmp[i-1]] - arr[tmp[i]])
        ans = max(tot, ans)
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
