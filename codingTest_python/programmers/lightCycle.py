def turnTow(turn, to):
    if to == 'L':
        turn += 1
    elif to == 'R':
        turn -= 1
    return turn % 4


def solution(grid):
    answer = []
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우상좌하
    cnt = 0
    sizeX, sizeY = len(grid), len(grid[0])

    for i in range(len(grid)):
        grid[i] = list(grid[i])

    visited = [[[False]*4 for _ in range(sizeY)] for _ in range(sizeX)]

    for x in range(sizeX):
        for y in range(sizeY):
            for i in range(4):
                if visited[x][y][i]:
                    continue
                # print(x, y, visited)
                cnt = 0
                rx, ry, turn = x, y, i
                while True:
                    print(rx, ry, turn)
                    visited[rx][ry][turn] = True
                    rx = (rx + direction[turn][0]) % sizeX
                    ry = (ry + direction[turn][1]) % sizeY
                    turn = turnTow(turn, grid[rx][ry])
                    cnt += 1
                    if turn == i and rx == x and ry == y:
                        break
                print('----------')
                answer.append(cnt)

    answer.sort()
    return answer
