import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())

parent = [0]*(n+1)
# parent 초기화
for i in range(n):
    parent[i] = i

graph = [[] for _ in range(n)]
stars = [list(map(float, input().split())) for _ in range(n)]

def find_parent(parent, v):
    if parent[v] != v:
        return find_parent(parent, parent[v])
    return parent[v]

def union_find(parent, a, b):
    a = find_parent(parent ,a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

stars.sort(key = lambda x:x[1])
edges = []

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()
result = 0


for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_find(parent, x, y)
        result += cost

print(round(result, 2))