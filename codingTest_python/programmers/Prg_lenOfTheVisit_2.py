def solution(dirs):
    direction = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y, rx, ry = 0, 0, 0, 0
    ans = set()

    for di in dirs:
        rx, ry = x + direction[di][0], y + direction[di][1]
        if -5 <= rx <= 5 and -5 <= ry <= 5:
            ans.add((rx, ry, x, y))
            ans.add((x, y, rx, ry))
            x, y = rx, ry
    return len(ans)//2
