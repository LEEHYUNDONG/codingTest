import sys
input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    m, n, x, y = map(int, input().rsplit())
    flag = True
    while (x <= m*n):
        if x % n == y % n:
            ans.append(x)
            flag = False
            break
        x += m
    if flag:
        ans.append(-1)


for i in ans:
    print(i)
