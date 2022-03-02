import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth = list(map(int, input().split()))
parent = [i for i in range(n+1)]


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


for i in truth[1:]:
    union_find(parent, i, 0)


res = 0
edge = []

for _ in range(m):
    tmp = list(map(int, input().split()))
    edge.append(tmp)

edge.sort(reverse=True)


for i in edge:
    tmp = i[1:]
    for j in range(len(tmp)-1):
        if find_parent(parent, tmp[j]) != find_parent(parent, tmp[j+1]):
            union_find(parent, tmp[j], tmp[j+1])
        
for i in edge:
    tmp = i[1:]
    for j in tmp:
        if find_parent(parent, j) == 0:
            break
    else:
        res += 1
print(res)