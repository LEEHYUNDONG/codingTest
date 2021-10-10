from collections import deque
# ㄷㅔ이터 입력
n, m = map(int, input().split())
#direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
rx = [-1, 0, 1, 0]
ry = [0, 1, 0, -1]
x, y, t = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

q = deque([])
q.append([x, y])
graph[x][y] = 1
cnt = 1

while True:
    x, y = q.popleft()
    check = False
    for i in range(4):
        t = (t - i) % 4
        dx, dy = x+rx[t], y+ry[t]
        print(dx, dy, check)
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] == 0:
                cnt += 1
                check = True
                q.appendleft([dx, dy])
                graph[dx][dy] = 2
                break
    if not check:
        dx, dy = x-rx[t], y-ry[t]
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dx][dy] == 2:
                q.appendleft([dx, dy])
            if graph[dx][dy] == 1:
                break
        else:
            break

print(cnt)
