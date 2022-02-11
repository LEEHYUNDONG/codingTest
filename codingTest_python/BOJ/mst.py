import sys
input = sys.stdin.readline

v, e = map(int, input().split())

parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = [list(map(int, input().split())) for _ in range(e)] 
edges.sort(key = lambda x : x[2])
ans = 0

for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        ans += c
print(ans)


