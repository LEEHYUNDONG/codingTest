n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]


def bitMask():
    res = 0

    for i in range(1 << n*m):
        total = 0
        for row in range(n):
            srow = 0
            for col in range(m):
                idx = row * m + col
                if i & (1 << idx) != 0:
                    srow = srow * 10 + arr[row][col]
                else:
                    total += srow
                    srow = 0
            total += srow

        for col in range(m):
            scol = 0
            for row in range(n):
                idx = row * m + col
                if i & (1 << idx) == 0:
                    scol = scol * 10 + arr[row][col]
                else:
                    total += scol
                    scol = 0

            total += scol
        res = max(res, total)
    return res


print(bitMask())

# 아이디어: 배열의 가로, 세로 연산 여부를 0, 1로 나누어 1이면 가로계산에
# 0이면 세로 계산에 이용한다.
# 각 열, 행을 순회하며 1이 이어지면 왼쪽으로 한칸씩 늘려주면 누적합의 자릿수를
# 늘려주고 0이 나오면 자릿수를 초기화시키는 형식
