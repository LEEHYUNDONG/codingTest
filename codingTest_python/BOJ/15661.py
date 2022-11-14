import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
tmp = []
ent = set()

def dfs(depth):
    if 1 <= depth and depth < N:

        print(t1, t2)
        return
    
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            tmp.append(i)
            dfs(depth+1)
            tmp.pop()
            visited[i] = False


dfs(0)