from collections import deque

n, m = map(int, input().split())
q = deque([])
q.append(n)
visited = [-1] * 200001
visited[n] = 0

while q:
    loc = q.popleft()
    if loc == m:
        print(visited[loc])
        break
    if loc*2 <= 200000 and visited[2*loc] == -1:
        q.appendleft(2*loc)
        visited[2*loc] = visited[loc]
    if 0 <= loc-1 and visited[loc-1] == -1:
        q.append(loc-1)
        visited[loc-1] = visited[loc]+1
    if loc+1 <= 200000 and visited[loc+1] == -1:
        q.append(loc+1)
        visited[loc+1] = visited[loc]+1