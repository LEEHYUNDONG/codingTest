from collections import deque


def solution(board):
    answer = int(1e9)
    visited = [[int(1e9)]*len(board) for _ in range(len(board))]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우

    q = deque([[0, 0, 0, 0, 0]])  # x, y, rx, ry, cost
    visited[0][0] = 0

    while q:
        x, y, px, py, cost = q.popleft()  # 현재 위치, 이전 노드 , 비용
        if x == len(board)-1 and y == len(board)-1:
            answer = min(cost, answer)

        for rx, ry in direction:
            new_flag = 0
            dx, dy = x + rx, y + ry
            tmp = 0
            if 0 <= dx < len(board) and 0 <= dy < len(board) and board[dx][dy] == 0:

                if px == dx or py == dy:
                    pay = 100
                else:
                    pay = 600
                # 이부분 해결해야됨
                if visited[dx][dy] < cost + pay:
                    continue
                if visited[dx][dy] == cost + pay:
                    pay = 100
                q.append([dx, dy, x, y, cost+pay])
                visited[dx][dy] = cost + pay

    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == int(1e9):
                print('XXXX', end=' ')
            else:
                print(visited[i][j], end=' ')
        print()

    return answer
