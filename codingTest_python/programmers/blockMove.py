from collections import deque


def solution(board):
    answer = 10000000
    dest = len(board)
    head, tail = [0, 0], [0, 1]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 회전은 나 기준 아래 두칸이나 옆 두칸이 모두 0일때 가능하다

    visited = [[[-1]*dest for _ in range(dest)] for _ in range(2)]
    q = deque([[head, tail, 0, 0]])  # cnt, mode

    visited[0][0][0] = 0
    visited[0][0][1] = 0
    while q:
        head, tail, mode, cnt = q.popleft()  # mode 0 가로, mode 1 세로
        hx, hy = head
        tx, ty = tail
        if (hx == dest-1 and hy == dest-1) or (tx == dest-1 and ty == dest-1):
            answer = min(cnt, answer)
            break

        for rx, ry in directions:
            hdx, hdy = hx + rx, hy + ry
            tdx, tdy = tx + rx, ty + ry
            if 0 <= hdx < dest and 0 <= hdy < dest and 0 <= tdx < dest and 0 <= tdy < dest:
                if board[hdx][hdy] == 0 and board[tdx][tdy] == 0:

                    if visited[mode][hdx][hdy] == -1 or visited[mode][tdx][tdy] == -1:
                        q.append([[hdx, hdy], [tdx, tdy], mode, cnt + 1])
                        visited[mode][hdx][hdy] = visited[mode][tx][ty] + 1
                        visited[mode][tdx][tdy] = visited[mode][tx][ty] + 1

                    # 가로에서 세로로
                    if mode == 0:
                        q.append([[tdx, tdy], [tx, ty], 1, cnt + 1])
                        q.append([[hx, hy], [hdx, hdy], 1, cnt + 1])
                        visited[1][tdx][tdy] = visited[1][tx][ty] + 1
                        visited[0][hdx][hdy] = visited[0][hx][hy] + 1
                        visited[1][tx][ty] += 1
                    # 세로에서 가로로

                    elif mode == 1:
                        if visited[0][tdx][tdy] == -1:
                            q.append([[tdx, tdy], [tx, ty], 0, cnt + 1])
                            visited[0][tdx][tdy] = visited[1][tx][ty] + 1
                        elif visited[0][hdx][hdy] == -1:
                            q.append([[hx, hy], [hdx, hdy], 0, cnt + 1])
                            visited[0][hdx][hdy] = visited[0][hx][hy] + 1

                        visited[0][tx][ty] += 1

    return answer
