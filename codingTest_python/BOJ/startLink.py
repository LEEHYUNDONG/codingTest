from collections import deque
f, s, g, u, d = map(int, input().split()) # s에서 g층으로


def bfs(start, u, d, g, f):
    q = deque([])
    visited = [-1]*(2000001)
    q.append(start)
    visited[start] = 0
    
    while q:
        x = q.popleft()
        if x == g:
            return visited[x]
        if x+u <= f and visited[x+u] == -1 and u!=0:
            q.append(x+u)
            visited[x+u] = visited[x]+1
        if 1<=x-d and visited[x-d] == -1 and d!=0:
            q.append(x-d)
            visited[x-d] = visited[x]+1

    return "use the stairs"

print(bfs(s, u, d, g, f))