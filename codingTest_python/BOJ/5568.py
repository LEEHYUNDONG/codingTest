import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

lst = [input().rstrip() for _ in range(N)]
ans = set()
cnt = 0
visited = [False for _ in range(N)]

def dfs(num, depth):
    global cnt
    if depth == K and num not in ans:
        ans.add(num)
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(num + lst[i], depth + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(lst[i], 1)
    visited[i] = False

print(cnt)