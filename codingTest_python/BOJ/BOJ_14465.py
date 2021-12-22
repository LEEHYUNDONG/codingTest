import sys
from collections import deque
input = sys.stdin.readline

n, k, b = list(map(int, input().split()))
broken = [0 for _ in range(200001)]
res = int(1e9)
cnt = 0

for i in range(b):
    tmp = int(input())
    broken[tmp+k] = 1

for i in range(1, n+1):
    cnt += broken[i+k]
    cnt -= broken[i]
    if i >= k and cnt < res:  # 최솟값 찾아주기 와 i가 k보다 커야한다.
        res = cnt
print(res)
