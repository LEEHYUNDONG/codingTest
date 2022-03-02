import sys
input = sys.stdin.readline
t = int(input())
INF = int(1e9)


def bellmanFord():
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            for t, e in graph[j]:
                if distance[j] + t < distance[e]:
                    distance[e] = distance[j]+t
                    if i == N:
                        return False
    return True

for _ in range(t):
    N, M, W = map(int, input().split())

    INF = 2147483647
    distance = [INF for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((T, E))
        graph[E].append((T, S))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((-T, E))
    

    if bellmanFord():
        print('NO')
    else:
        print('YES')