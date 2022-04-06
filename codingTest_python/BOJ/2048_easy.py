import sys
import copy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def checkSame(board, n):
    maxV = -1
    lst = []
    ttmp = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                maxV = max(board[i][j], maxV)
                lst.append([i, j])
                ttmp.append(board[i][j])
                cnt += 1

    if len(ttmp) != len(set(ttmp)):
        return True, lst
    else:
        return False, maxV
            

def move_block(board, d):
    tmp = copy.deepcopy(board)
    flag, lst = checkSame(tmp, n)
    if not flag:
        return lst
    lst.sort()
    print(lst)
    if d == 1: # 위
    

    # elif d == 2: # 아래



move_block(board, 1)