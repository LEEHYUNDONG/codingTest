def solution(n, m, x, y, r, c, k):
    answer = []
    move = ['l', 'r', 'd', 'u']
    directions = {'l' : (0, -1), 'r' : (0, 1), 'd':(1, 0), 'u':(-1, 0)}

    # init board
    board = [[0]*m for _ in range(n)]
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    board[x][y] = 1
    board[r][c] = n*m
    
    # Out of block
    def OOB(rx, ry):
        return (0 <= rx < n) and (0<= ry < m)
    
    def dfs(tmp, x, y, depth):
        if depth > k:
            return
        # if depth == k and x == r and y == c:
        if depth == k:
            answer.append(tmp)
            print(tmp)
            return
        for i in range(4):
            rx = x + directions[move[i]][0]
            ry = y + directions[move[i]][1]
            if not OOB(rx, ry):
                dfs(tmp + move[i], rx, ry, depth+1)

    dfs('', x, y, 0)
    print(answer)

    
    
    return answer