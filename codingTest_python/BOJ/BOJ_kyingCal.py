import sys
input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n, m, x, y = map(int, input().rsplit())
    l, r = 1, 1
    cnt = 1
    while True:
        if l == x and r == y:
            ans.append(cnt)
            break
        if l >= n and r >= m:
            ans.append(-1)
            break
        if l < n and r < m:
            l += 1
            r += 1
        elif l < n and r == m:
            r = 1
            l += 1
        elif l == n and r < m:
            l = 1
            r += 1
        elif l == n and r == m:
            r = 1
            l = 1
        cnt += 1

for i in ans:
    print(i)

# 15
# 40000 39999 39999 39998
# 40000 39999 40000 39999
# 40000 40000 40000 39999
# 40000 39998 40000 39997
# 39999 2 39998 2
# 3 40000 3 39999
# 40000 3 40000 3
# 8 2 4 2
# 10 12 2 12
# 12 10 12 10
# 12 10 1 1
# 12 6 12 6
# 10 1 5 1
# 1 10 1 5
# 1 1 1 1

# 답
# 1599959999
# 1599960000
# -1
# -1
# 39998
# 39999
# 120000
# 4
# 12
# 60
# 1
# 12
# 5
# 5
# 1
