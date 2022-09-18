import sys
input = sys.stdin.readline

N = int(input())
dat = []
sentinel = 0

for _ in range(N):
    x, a = map(int, input().split())
    sentinel += a
    dat.append([x, a])

dat.sort(key = lambda x :x[0])

cnt, answer = 0, 0
sentinel /= 2

for i in range(N):
    cnt += dat[i][-1]
    if cnt >= sentinel:
        answer = dat[i][0]
        break

print(answer)