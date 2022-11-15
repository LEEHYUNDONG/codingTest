import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
tmp = []
ans = 100000000

def find():
    global ans
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start += graph[i][j]
            elif not visited[i] and not visited[j]:
                link += graph[i][j]
    ans = min(ans, abs(start-link))
    return

def dfs(depth):
    if depth == N:
        find()
        return
    

    visited[depth] = True
    dfs(depth+1)
    visited[depth] = False
    dfs(depth+1)

dfs(0)


print(ans)