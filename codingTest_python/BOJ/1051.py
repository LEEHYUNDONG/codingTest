import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 둘중에 짧은 길이 만큼 탐색을 하면 됨
def check(x, y, size):
    global ans
    if x + size >= N and y + size >= M:
        return
    shape = graph[x][y]
    if graph[x+size][y] == shape and graph[x][y+size] == shape and graph[x+size][y+size] == shape:
        ans = max((size+1)**2, ans)

max_len = min(N, M)
ans = 0

for i in range(N):
    for j in range(M):
        for size in range(max_len+1):
            if i + size >= N or j + size >= M:
                continue
            check(i, j, size)
print(ans)