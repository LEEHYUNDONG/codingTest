
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(x, y):
            if x >= r or x < 0 or y >= c or y < 0:
                return False
            return True

        def dfs(x, y, index):
            if len(word) - 1 == index:
                return True
            for rx, ry in direction:
                dx, dy = x + rx, y + ry
                if isValid(dx, dy) and not visited[dx][dy] and board[dx][dy] == word[index+1]:
                    visited[dx][dy] = True
                    if dfs(dx, dy, index+1):
                        return True
                    visited[dx][dy] = False
            return False
        visited = [[False for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j]:
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False
        return False
