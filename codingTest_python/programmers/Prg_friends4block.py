def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    print(board)
    cnt = 0
    rm = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                c = board[i][j]
                if c == []:
                    continue
                if board[i+1][j] == c and board[i][j+1] == c and board[i+1][j+1] == c:
                    rm.add((i, j))
                    rm.add((i+1, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j+1))
        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = []
            print(board[i][j])
            rm = set()
        else:
            return cnt
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break
