def solution(dirs):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    toward = 0
    ans = set()
    x, y, rx, ry = 0, 0, 0, 0

    for di in dirs:
        if di == 'U':
            toward = 0
        elif di == 'D':
            toward = 1
        elif di == 'R':
            toward = 2
        else:
            toward = 3

        rx = x+dx[toward]
        ry = y+dy[toward]
        if rx > 5 or rx < -5 or ry < -5 or ry > 5:
            rx, ry = x, y
            continue
        if (rx, ry, x, y) not in ans and (x, y, rx, ry) not in ans:
            ans.add((rx, ry, x, y))
        x, y = rx, ry

    print(ans)
    return len(ans)
