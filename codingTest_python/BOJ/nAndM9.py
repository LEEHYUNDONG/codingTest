import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
visited = [False for _ in range(n)]
ans = set()

def dfs(idx, tmp, depth):
    global ans
    if depth == m:        
        
        ans.add(tuple(tmp))
        return
    
    for i in range(n):
        if not visited[i]:
            tmp.append(arr[i])
            visited[i] = True
            dfs(i, tmp, depth+1)
            tmp.pop(-1)
            visited[i] = False


dfs(0, [], 0)

ans = list(ans)
ans.sort()
for i in ans:
    print(*i)