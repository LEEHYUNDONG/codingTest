import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = int(1e9)
    distance = [[INF]*(n+1) for _ in range(n+1)]
    
    
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append([d, f])
        graph[d].append([c, f])
        
    def dijkstra(start):
        q = []
        distance[start][start] = 0
        heapq.heappush(q, [0, start])
        while q:
            dist, v = heapq.heappop(q)
            if dist < distance[start][v]:
                    continue
            for i in graph[v]:
                cost = i[1] + dist
                if cost <= distance[start][i[0]]:
                    heapq.heappush(q, [cost, i[0]])
                    distance[start][i[0]] = cost
    # dijkstra(s)
    answer = INF
    for i in range(1, n+1):
        dijkstra(i)
        
    for i in range(1, n+1):
        if i == s:
            continue
        # print(distance[s][i], distance[i][a], distance[i][b])
        answer = min(answer, distance[i][a]+distance[s][i]+distance[i][b])
        answer = min(distance[s][a]+distance[s][b], answer)
                
    return answer