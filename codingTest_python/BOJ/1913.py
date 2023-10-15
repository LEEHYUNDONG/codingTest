import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
destX, destY = 0, 0
num = N**2
res = [[0 for _ in range(N)] for _ in range(N)]


def findDest(x, y, target):
    global destX
    global destY
    if res[x][y] == target:
        destX, destY = x, y


for i in range(N):
    # 위에서 아래
    for j in range(i, N-i-1):
        res[j][i] = num
        findDest(j, i, M)
        num -= 1
    
    # 왼쪽에서 오른쪽
    for j in range(i, N - i - 1):
        res[N - i - 1][j] = num
        findDest(N-i-1, j, M)
        num -= 1

    # 아래에서 위
    for j in range(N - i - 1, i, -1):
        res[j][N-i-1] = num
        findDest(j, N-i-1, M)
        num -= 1

    # 오른쪽에서 왼쪽
    for j in range(N-i-1, i, -1):
        res[i][j] = num
        findDest(i, j, M)
        num -= 1


res[N//2][N//2] = 1
if M == 1:
    destX, destY = N//2, N//2

for i in range(N):
    print(*res[i])
print(destX+1, destY+1)