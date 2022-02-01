# def turnTow(turn, to):
#     if to == 'L':
#         turn += 1
#     elif to == 'R':
#         turn -= 1
#     return turn % 4


# def solution(grid):
#     answer = []
#     direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우상좌하
#     turn = 0
#     x, y = 0, 0
#     cnt = 0
#     sizeX, sizeY = len(grid), len(grid[0])

#     for i in range(len(grid)):
#         grid[i] = list(grid[i])

#     ans = []
#     visited = [[False] * len(grid[0]) for _ in range(len(grid))]
#     for i in range(4):
#         cnt = 0
#         turn = i
#         x, y = 0, 0
#         sx, sy = direction[turn][0], direction[turn][1]
#         start = grid[x][y]
#         way = ''
#         tmp = []
#         if not visited[x][y]:
#             while True:
#                 x = (x + direction[turn][0]) % sizeX
#                 y = (y + direction[turn][1]) % sizeY
#                 turn = turnTow(turn, grid[x][y])
#                 visited[x][y] = True
#                 cnt += 1
#                 tmp.append((grid[x][y], x, y))
#                 if grid[x][y] == start and direction[turn][0] == sx and direction[turn][1] == sy:
#                     if tmp not in ans:
#                         ans.append(tmp)
#                     break

#     if sizeX == 1 and sizeY == 1:
#         return [1, 1, 1, 1]
#     else:

#         for i in ans:
#             # print(i)
#             answer.append(len(i))
#         answer.sort()
#     return answer

def turnTow(turn, to):
    if to == 'L':
        turn += 1
    elif to == 'R':
        turn -= 1
    return turn % 4


def solution(grid):
    answer = []
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 우상좌하
    turn = 0
    x, y = 0, 0
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

                cnt = 0
                rx, ry, turn = x, y, i
                start = grid[rx][ry]
                while True:
                    visited[rx][ry][turn] = True
                    rx = (rx + direction[turn][0]) % sizeX
                    ry = (ry + direction[turn][1]) % sizeY
                    turn = turnTow(turn, grid[rx][ry])
                    cnt += 1
                    if turn == i and rx == x and ry == y:
                        break
                answer.append(cnt)

    answer.sort()
    return answer
