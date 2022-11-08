import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
start = int(input())

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