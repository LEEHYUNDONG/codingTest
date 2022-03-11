import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    

distance = [0 for _ in range(n+1)]

def dfs(start):
    for i in graph[start]:
        if distance[i[0]] == 0:
            distance[i[0]] = distance[start] + i[1]
            dfs(i[0])
            

dfs(1)

distance[1] = 0
idx = distance.index(max(distance))
distance = [0 for _ in range(n+1)]

dfs(idx)
distance[idx] = 0 # 루트는 출발지점은 무조건 0으로 초기화한다.11!!!!
print(max(distance))