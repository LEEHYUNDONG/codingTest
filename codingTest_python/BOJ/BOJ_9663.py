#n-queen
def check(x):
    for i in range(x):
        if col[i] == col[x] or abs(col[x] - col[i]) == x - i:
            return False
    return True

def nQueen(level):
    global cnt
    if level == n:
        cnt += 1
        return 
    for i in range(n):
        col[level] = i
        if check(level):
            nQueen(level+1)

n = int(input())
cnt = 0
col = [0]*n
nQueen(0)
print(cnt)
