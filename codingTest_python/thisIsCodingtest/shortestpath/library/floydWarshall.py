INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
