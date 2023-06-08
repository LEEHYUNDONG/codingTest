import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)

arr = [i for i in range(N)]

for r1 in combinations(arr, N//2):
    start, link = 0, 0
    r2 = list(set(arr) - set(r1))
    for r in combinations(r1, 2):
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]
    result = min(result, abs(start-link))

print(result)