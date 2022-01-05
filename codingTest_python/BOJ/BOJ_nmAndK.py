import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
graph = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y, tot, depth):
    if depth == k:
        global ans
        ans = max(tot, ans)
        return
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            flag = True
            if visited[i][j]:  # 중복 탐색을 방지한다
                continue
            for q in range(4):
                rx = i + dx[q]
                ry = j + dy[q]
                if 0 <= rx < n and 0 <= ry < m and visited[rx][ry]:
                    flag = False
                    break
            if flag:  # 상하좌우 방문 기록 없어야지 dfs로 탐색한다.
                visited[i][j] = True
                dfs(i, j, tot + graph[i][j], depth+1)
                visited[i][j] = False


visited = [[False] * m for _ in range(n)]
ans = -100000
dfs(0, 0, 0, 0)

print(ans)
