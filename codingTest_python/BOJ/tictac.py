import sys

input = sys.stdin.readline

def checkWinner(b, pat):

    for i in range(0, 7, 3):
        if b[i] == b[i+1] and b[i+1] == b[i+2] and pat == b[i]:
            return True

    for i in range(3):
        if b[i] == b[i+3] and b[i+3] == b[i+6] and pat == b[i]:
            return True
    
    if b[0] == b[4] and b[4] == b[8] and pat == b[0]:
        return True
        
    if b[2] == b[4] and b[4] == b[6] and pat == b[2]:
        return True
    return False

ans = []

while True:
    board = input().strip()
    if board == "end":
        break
    
    cntX, cntO = board.count('X'), board.count('O')
    if cntX > cntO + 1:
        ans.append("invalid")
        continue
    if cntO > cntX:
        ans.append("invalid")
        continue
    if cntX-1 == cntO:
        if checkWinner(board, 'X') and not checkWinner(board, 'O'):
            ans.append("valid")
            continue
    if cntO == cntX:
        if checkWinner(board, 'O') and not checkWinner(board, 'X'):
            ans.append("valid")
            continue
    if cntX == 5 and cntO == 4:
        if not checkWinner(board, 'O'):
            ans.append("valid")
            continue
    ans.append("invalid")

for i in ans:
    print(i)
    
    