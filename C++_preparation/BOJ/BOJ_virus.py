from collections import deque

n = int(input())
m = int(input())
virus = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0

for a, b in virus:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

q = deque([])
visited[0] = True
q.append(0)

while(q):
    x = q.popleft()
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            q.appendleft(y)
            cnt += 1

print(cnt)

