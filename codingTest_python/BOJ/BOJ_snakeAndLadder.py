from collections import deque

n, m = map(int, input().split())
graph = [i for i in range(101)]
visited = [False]*101

for _ in range(n + m):
    a, b = map(int, input().split())
    graph[a] = b

q = deque([[1, 0]])
visited[0] = True
visited[1] = True

while q:
    loc, cnt = q.popleft()
    if loc == 100:
        print(cnt)
        break
    for i in range(1, 7):
        if loc + i <= 100:
            if not visited[graph[loc+i]]:
                q.append([graph[loc+i], cnt+1])
                visited[graph[loc+i]] = True
