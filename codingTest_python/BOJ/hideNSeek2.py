from collections import deque

n, m = map(int, input().split())
q = deque([])
INF = int(1e9)

cnt = 0
q.append([n, 0])
visited = [-1 for _ in range(400001)]
visited[n] = 0

while q:
    x, t = q.popleft()
    if x == m:
        if visited[x] == t:
            cnt += 1
    if 2*x <= 200000 and (visited[2*x] == -1 or visited[2*x] >= visited[x]+1):
        q.append([2*x, visited[x] + 1])
        visited[2*x] = visited[x] + 1
    if x - 1 >= 0 and (visited[x-1] == -1 or visited[x-1] >= visited[x]+1):
        q.append([x-1, visited[x] + 1])
        visited[x-1] = visited[x] + 1
    if x + 1 <= 200000 and (visited[x+1] == -1 or visited[x+1] >= visited[x]+1):
        q.append([x+1, visited[x] + 1])
        visited[x+1] = visited[x] + 1


print(visited[m], cnt, sep="\n")