from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    def getIntensity():
        pq = [] # intensity, 현위치
        visited = [10000001]*(n+1)

        for gate in gates:
            heapq.heappush(pq, (0, gate))
            visited[gate] = 0
        
        while pq:
            intense, node = heapq.heappop(pq)

            if node in summitsSet or intense > visited[node]:
                continue
                
            for w, nextt in graph[node]:
                newIntense = max(intense, w)
                if newIntense < visited[nextt]:
                    visited[nextt] = newIntense
                    heapq.heappush(pq, (newIntense, nextt))
                        
        minV = [0, 10000001]
        
        for summ in summits:
            if visited[summ] < minV[1]:
                minV[0] = summ
                minV[1] = visited[summ]

        return minV
    
    summits.sort()
    summitsSet = set(summits)
    graph = defaultdict(list)

    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    return getIntensity()