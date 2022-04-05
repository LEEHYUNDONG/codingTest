
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ss = [input().strip() for _ in range(n)]
ss = set(ss)
cnt = 0


for _ in range(m):
    tmp = input().strip()
    if tmp in ss:
        cnt+=1

print(cnt)