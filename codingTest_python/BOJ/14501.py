import sys
input = sys.stdin.readline
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

ans = -1000

def dfs(idx, tot):
    global ans
    if idx == N:
        ans = max(tot, ans)
        return
    
    if schedules[idx][0] + idx <= N:
        dfs(idx+schedules[idx][0], tot + schedules[idx][-1])
    
    dfs(idx+1, tot)

dfs(0, 0)
print(ans)