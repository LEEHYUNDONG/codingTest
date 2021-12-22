n, k = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
graph = [[] for _ in range(n)]
visited = [False if i == k else True for i in range(n)]
mind = [INF]

def dfs(r, c, time, depth):
    if depth == n-1:
        mind[0] = min(mind[0], time)
    if time > mind[0]:
        return
    for j in range(n):
        if j != c and visited[j]:
            visited[j] = False
            dfs(c, j, time+planet[c][j], depth+1)
            visited[j] = True

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            planet[i][j] = min(planet[i][j], planet[i][k] + planet[k][j])

for c in range(n):
    if k != c and visited[c]:
        visited[c] = False
        dfs(k, c, planet[k][c], 1)
        visited[c] = True

print(mind[0])