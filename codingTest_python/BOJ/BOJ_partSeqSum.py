n, tot = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
visited = [False] * n
res = []
tmp = []


def dfs(idx, t, depth):
    global tmp, cnt
    if tot == t and depth >= 1:
        cnt += 1
    if depth == n:
        return
    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = True
        tmp.append(i)
        dfs(i, t + num[i], depth+1)
        tmp.pop()
        visited[i] = False


dfs(0, 0, 0)
print(cnt)
