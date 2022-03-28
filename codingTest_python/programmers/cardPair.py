from collections import deque
import copy


def solution(board, r, c):
    answer = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4가지 키 방향

    def checkCard(board):
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    return False
        return True

    def bfs(board, r, c):
        tmp = int(1e9)
        pos = []
        q = deque([])
        q.append([r, c, board[r][c]])
        graph = copy.deepcopy(board)
        visited = [[-1]*4 for _ in range(4)]

        character = graph[r][c]
        if character != 0:
            board[r][c] = 0
            visited[r][c] = 1
        else:
            visited[r][c] = 0
        flag = False
        while q:
            x, y, color = q.popleft()
            nx, ny = x, y
            if color != 0 and character == 0:
                character = color
                r, c = x, y
                board[r][c] = 0
                visited[r][c] = visited[x][y] + 1
                flag = True

            if board[x][y] == character and color != 0 and visited[x][y] != 0:
                board[x][y] = 0
                # visited[x][y] += 1
                if flag:
                    tmp = visited[x][y] + visited[r][c] + 1
                else:
                    tmp = visited[x][y]
                pos = [x, y, tmp]
                # print("r, c, x, y:", r, c, x, y)
                # print("visited[r][c], visited[x][y] :", visited[r][c], visited[x][y])
            for rx, ry in directions:
                dx, dy = rx + x, ry + y
                if 0 <= dx < 4 and 0 <= dy < 4:
                    if visited[dx][dy] == -1 or visited[dx][dy] > visited[x][y] + 1:
                        q.append([dx, dy, board[dx][dy]])  # 한칸씩 움직이는 경우
                        visited[dx][dy] = visited[x][y] + 1
                        # if character == 0 and board[dx][dy] != 0:
                        #     visited[dx][dy] += 1

                    while True:  # ctrl + dir인 경우, 여러 칸
                        nx += rx
                        ny += ry
                        if 0 > nx or nx >= 4 or ny < 0 or ny >= 4:
                            nx -= rx
                            ny -= ry
                            break
                    if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                        q.append([nx, ny, board[nx][ny]])
                        visited[nx][ny] = visited[x][y] + 1

        return pos

    while True:
        if checkCard(board):
            break
        for i in range(4):
            print(*board[i])

        r, c, tmp = bfs(board, r, c)
        print("operations :", tmp)
        answer += tmp

    return answer
