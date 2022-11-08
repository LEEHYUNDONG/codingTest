import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
arr = list(map(int, input().split()))
start = int(input())


for i, parent in enumerate(arr, 0):
    if parent == -1:
        continue
    else:
        tree[parent].append(i)


def dfs(v):
    arr[v] = -2
        
    for i in range(len(arr)):
        if v==arr[i]:
            dfs(i)

dfs(start)
ans = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        ans += 1

print(ans)