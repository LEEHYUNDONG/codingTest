from collections import deque
import sys
input = sys.stdin.readline


class Solution:
    def bfs(i, j, visited):
        q = deque([])
        q.append([i, j])
        visited[i][j] = True
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        while q:
            x, y = q.popleft()
            for i in range(4):
                rx, ry = x + dx, y + dy
                if 0 <= rx < r and 0 <= ry < c:
                    if not visited[rx][ry]:

    def exist(self, board: List[List[str]], word: str) -> bool:

        r, c = len(board), len(board[0])
        print(r, c)
        for i in range(r):
            for j in range(c):
                visited = [[False for _ in range(len(board))]
                           for _ in range(len(board[0]))]

        while q:
