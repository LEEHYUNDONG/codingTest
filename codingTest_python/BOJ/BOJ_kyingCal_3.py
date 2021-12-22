import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    flag = True
    while x <= m*n:
        if x % n == y % n:
            flag = False
            print(x)
            break
        x += m
    if flag:
        print(-1)
