import sys
input = sys.stdin.readline

n, L = map(int, input().split())

ans = 0
graph = [list(map(int, input().split())) for _ in range(n)]

def checkRoute(n, L, graph):
    visited = [0]*n
    for i in range(n-1):
        if graph[i] != graph[i+1]:
            if abs(graph[i] - graph[i+1]) > 1: # 높이 차이 1 이상 break
                return False
            else:            
                if graph[i] > graph[i+1]: # 왼쪽이 큰경우
                    if i+1+L > n:
                        return False
                    tmp = graph[i+1]
                    for j in range(i+1, i+1+L):
                        if visited[j] or graph[j] != tmp:
                            return False
                        visited[j] = 1

                elif graph[i] < graph[i+1]: # 오른쪽이 큰경우
                    if i-L < -1:
                        return False
                    tmp = graph[i]
                    for j in range(i, i-L, -1):
                        if visited[j] or graph[j] != tmp:
                            return False
                        visited[j] = 1

    return True


for g in graph:
    if checkRoute(n, L, g):
        ans += 1

for g in range(n):
    if checkRoute(n, L, [graph[i][g] for i in range(n)]):
        ans += 1
print(ans)
