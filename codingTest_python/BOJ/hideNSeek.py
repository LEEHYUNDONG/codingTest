# from collections import deque

# n, m = map(int, input().split())
# q = deque([])
# q.append([n, 0])
# INF = int(1e9)
# visited = [INF] * max(m+1, n+1)

# while q:
#     loc, time = q.popleft()
#     if loc == m:
#         print(visited[loc])
#         break
#     if loc*2 <= m:
#         q.appendleft([2*loc, time])
#         visited[2*loc] = min(time, visited[2*loc])
#     if 1 <= loc <= m-1:
#         q.append([loc+1, time+1])
#         q.append([loc-1, time+1])
#         visited[loc-1] = min(time+1, visited[loc-1])
#         visited[loc+1] = min(time+1, visited[loc+1])


from collections import deque
MAX = 100001
check = [False] * MAX
dist = [-1] * MAX

n,k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 <= MAX and check[now*2] == False:  # 순간이동
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 <= MAX and check[now+1] == False: # x+1이동
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and check[now-1] == False: # x-1이동
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1

print(dist[k])