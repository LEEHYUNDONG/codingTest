import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def init():
    visited = [False for _ in range(N)]

    return visited

def dfs(a, b, dist):
    if a == b:
        ans = dist
        return
    for i in graph[a]:
        if not visited[i[0]]:
            dfs(i, b, dist+i[-1])

for _ in range(M):
    a, b = map(int, input().split())
    ans = 0
    visited = init()
    print(ans)

