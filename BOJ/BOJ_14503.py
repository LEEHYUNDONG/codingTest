# ㄷㅔ이터 입력
n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

graph[r][c] = 2
cnt = 1
x, y = r, c


def turnL():
    global t
    t = (t-1) % 4


while True:
    check = False
    for _ in range(4):
        turnL()
        rx, ry = x+dx[t], y+dy[t]
        #print(dx, dy, check)
        if 0 <= rx < n and 0 <= ry < m:
            if graph[rx][ry] == 0:

                cnt += 1
                graph[rx][ry] = 2
                x, y = rx, ry
                check = True
                break
    if not check:
        nx, ny = x-dx[t], y-dy[t]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:
                x, y = nx, ny
            elif graph[nx][ny] == 1:
                break
        else:
            break


print(cnt)
