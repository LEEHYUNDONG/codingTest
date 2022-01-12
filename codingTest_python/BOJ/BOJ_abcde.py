import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, v, visited, depth):
    if depth == 4:
        print(1)
        exit()

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited, depth+1)
            visited[i] = False


for i in range(n):
    visited = [False]*(n)
    visited[i] = True
    dfs(graph, i, visited, 0)
    visited[i] = False

print(0)
