from collections import deque
import sys
input = sys.stdin.readline


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        cnt = 0
        w = deque(word)
        for i in range(r):
            for j in range(c):
                visited = [[False for _ in range(r)] for _ in range(c)]
                if w[0] == board[i][j]:
                    q = deque([])
                    q.append([i, j])
                    visited[i][j] = True
                    w.popleft()
                    cnt += 1
                    while q:
                        x, y = q.popleft()
                        for i in range(4):
                            rx, ry = x + dx[i], y + dy[i]
                            if 0 <= rx < r and 0 <= ry < c:
                                if not visited[rx][ry] and w[0] == board[rx][ry]:
                                    w.popleft()
                                    cnt += 1
                                    visited[rx][ry] = True
                                    q.append([rx, ry])
                if w:
                    w = deque(word)
                elif not w:
                    return True
        return False
