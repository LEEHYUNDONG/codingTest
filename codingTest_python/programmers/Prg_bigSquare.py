def solution(board):
    rows, cols = len(board), len(board[0])
    cnt = 0
    tmp = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                continue
            for q in range(1, min(rows, cols)+1):
                tmp = 0
                if i + q <= rows and j + q <= cols:
                    flag = False
                    for k in range(i, i+q):
                        for l in range(j, j+q):
                            if board[k][l] == 1:
                                tmp += 1
                            else:
                                flag = True
                                break
                        if flag:
                            break
                    if flag:
                        break

                    cnt = max(cnt, tmp)

    return cnt
