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
    
    for i in range(idx, n):
        tmp.append(arr[i])
        dfs(i, tmp, depth+1)
        tmp.pop(-1)
        


dfs(0, [], 0)

ans = list(ans)
ans.sort()

for i in ans:
    print(*i)