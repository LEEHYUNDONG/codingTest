import sys
from collections import deque

input = sys.stdin.readline

tob = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    tob.append(deque(tmp))

N = int(input())
test = [list(map(int, input().split())) for _ in range(N)]

