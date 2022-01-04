import sys
from collections import deque
from itertools import combinations


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = deque([])
ans = []
house = deque([])

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        if graph[i][j] == 1:
            house.append([i, j])

minv = float('inf')
tot = 0

for i in combinations(chicken, m):
    tot = 0
    dist = []
    for j in house:
        # 이부분에서 치킨집 중에서 한ㄴ 집까지 거리 중에서 최소가 되는 값을 찾음
        tot += min([abs(ch[0] - j[0]) + abs(ch[1]-j[1]) for ch in i])
        if minv <= tot:
            break
    if tot < minv:
        minv = tot

print(minv)
