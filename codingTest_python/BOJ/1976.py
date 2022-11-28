import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

#initialize

parent = [i for i in range(N+1)]

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        
        if graph[i][j] == 0:
            continue
        union_parent(parent, i+1, j+1)

lst = list(map(int, input().split()))

p = find_parent(parent, lst[0])

def answer():
    for i in range(1, M):
        if p != find_parent(parent, lst[i]):
            return "NO"
    return "YES"

print(answer())