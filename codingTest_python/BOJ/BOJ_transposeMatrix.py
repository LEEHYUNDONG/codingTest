from os import TMP_MAX
import sys
input = sys.stdin.readline


def cal1(arr):
    return arr[::-1]


def cal2(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return arr


def cal3(arr, n, m):
    tmp = [[0] * n for _ in range(m)]
    for i in range(m):  # 열
        for j in range(n):  # 행
            tmp[i][j] = arr[n-1-j][i]  # 행렬의 끝점에서부터 채워 나감.
    return tmp


def cal4(arr, n, m):
    tmp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            tmp[i][j] = arr[j][m-1-i]
    return tmp


def cal5(arr, n, m):
    tmp = [[0] * m for _ in range(n)]

    #제 1사분면 -> 2사분면
    for i in range(n//2):
        for j in range(m//2):
            tmp[i][m//2 + j] = arr[i][j]
    #제 2사분면 -> 4사분면
    for i in range(n//2):
        for j in range(m//2, m):
            tmp[(n//2)+i][j] = arr[i][j]
    # #제 3사분면 ->
    for i in range(n//2, n):
        for j in range(m//2):
            tmp[i-n//2][j] = arr[i][j]

    #제 4사분면
    for i in range(n//2, n):
        for j in range(m//2, m):
            tmp[i][j-m//2] = arr[i][j]

    return tmp


def cal6(arr, n, m):
    tmp = [[0] * m for _ in range(n)]

    #제 1사분면 -> 4사분면
    for i in range(n//2):
        for j in range(m//2):
            tmp[i+n//2][j] = arr[i][j]
    #제 2사분면 -> 1사분면
    for i in range(n//2):
        for j in range(m//2, m):
            tmp[i][j-m//2] = arr[i][j]
    # # #제 3사분면 -> 4사분면
    for i in range(n//2, n):
        for j in range(m//2):
            tmp[i][j+m//2] = arr[i][j]

    # #제 4사분면 -> 2 사분면
    for i in range(n//2, n):
        for j in range(m//2, m):
            tmp[i-n//2][j] = arr[i][j]

    return tmp


n, m, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
oper = list(map(int, input().split()))


for op in oper:
    n, m = len(arr), len(arr[0])
    if op == 1:
        arr = cal1(arr)
    elif op == 2:
        arr = cal2(arr)
    elif op == 3:
        arr = cal3(arr, n, m)
    elif op == 4:
        arr = cal4(arr, n, m)
    elif op == 5:
        arr = cal5(arr, n, m)
    elif op == 6:
        arr = cal6(arr, n, m)

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()
