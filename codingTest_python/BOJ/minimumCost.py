import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

distance = [sys.maxsize]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    
start, end = map(int, input().split())

move = [0 for _ in range(n+1)]
ans = []

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, x = heapq.heappop(q)
        if dist > distance[x]:
            continue
        for i in graph[x]:
            cost = dist + i[0]
            if cost >= distance[i[1]]: ### 이부분이 메모리 초과 유발
                continue
            if cost < distance[i[1]]:
                move[i[1]] = x
                distance[i[1]] = cost
                heapq.heappush(q, [cost, i[1]])


dijkstra(start, distance)

tmp = end
while tmp:
    ans.append(tmp)
    tmp = move[tmp]

print(distance[end])
print(len(ans))

print(' '.join(map(str, ans[::-1])))