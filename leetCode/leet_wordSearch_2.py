r = 0
c = 0
visited = []


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        l = len(word)
        dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isValid(x, y):
            if x < 0 or x >= r or y < 0 or y >= c:
                return False
            return True

        def dfs(i, j, index):
            if len(word)-1 == index:
                return True
            for dx, dy in dire:
                rx, ry = i + dx, j + dy
                if isValid(rx, ry) and not visited[rx][ry] and word[index+1] == board[rx][ry]:
                    visited[rx][ry] = True
                    if dfs(rx, ry, index+1):
                        return True
                    visited[rx][ry] = False
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False
        return False
