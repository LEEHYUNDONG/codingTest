from collections import deque


def solution(places):
    answer = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(i, j, visited):
        q = deque([])
        q.append([i, j, 0])
        visited[i][j] = True
        while q:
            x, y, dist = q.popleft()
            for rx, ry in directions:
                dx, dy = x + rx, y + ry
                if 0 <= dx < 5 and 0 <= dy < 5:
                    if not visited[dx][dy] and place[dx][dy] != 'X':
                        if place[dx][dy] == 'P' and dist + 1 <= 2:
                            return False
                        q.append([dx, dy, dist + 1])
                        visited[dx][dy] = True

        return True

    for place in places:
        tmp = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    tmp.append([i, j, 0])
        flag = False
        for i, j, dist in tmp:
            visited = [[0]*5 for _ in range(5)]
            if not bfs(i, j, visited):
                flag = True
                break
        if not flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer
