from collections import deque
# ㄷㅔ이터 입력
n, m = map(int, input().split())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
x, y, t = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

q = deque([])
q.append([x, y, t])
graph[x][y] = 1
cnt = 1

while q:
    x, y, t = q.popleft()
    move = 0
    for i in range(4):
        toward = (t - i) % 4
        rx, ry = direction[toward]
        dx, dy = x+rx, y+ry
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] != 0:
                continue
            if graph[dx][dy] == 0:
                cnt += 1
                q.appendleft([dx, dy, toward-1])
                graph[dx][dy] = cnt
            else:
                move += 1
    if move == 4:
        mp = 0
        x, y, t = x-direction[t][0], y-direction[t][0], t
        if 0 <= x < n and 0 <= y < m:
            if graph[x][y] != 0:
                break
        if 0 > x or x >= n or 0 > y or y >= n:
            break
        for i in range(4):
            toward = (t - i) % 4
            dx, dy = direction[toward][0]+x, direction[toward][1]+y
            if dx < 0 and dx >= n and dy < 0 and dy >= m:
                mp += 1
            elif 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] != 0:
                    mp += 1
                elif graph[dx][dy] == 0:
                    q.appendleft([dx, dy, toward-1])
                    cnt += 1
                    graph[dx][dy] = cnt

            if mp == 4:
                break
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
print(cnt)
