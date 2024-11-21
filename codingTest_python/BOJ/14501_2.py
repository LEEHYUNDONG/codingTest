import sys
input = sys.stdin.readline

N = int(input())
workData = [list(map(int, input().split())) for _ in range(N)]
result = [0 for _ in range(N)]
ans = -10000

def dfs(idx, tot):
    global ans
    if idx == N:
        ans = max(ans, tot)
        return

    if idx + workData[idx][0] <= N:
        dfs(idx+workData[idx][0], tot + workData[idx][-1])
    
    dfs(idx+1, tot)

dfs(0, 0)

print(ans)