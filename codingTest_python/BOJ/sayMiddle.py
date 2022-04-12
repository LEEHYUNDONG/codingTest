import sys
import heapq

input = sys.stdin.readline


n = int(input())
maxq, minq = [], [] #왼쪽 큐, 오른쪽 큐

for i in range(n):
    tmp = int(input())
    if len(maxq) == len(minq):
        heapq.heappush(maxq, -tmp)
    else:
        heapq.heappush(minq, tmp)
    
    if len(maxq) >= 1 and len(minq) >= 1 and maxq[0]*-1 > minq[0]:
        maxV = heapq.heappop(maxq)*-1
        minV = heapq.heappop(minq)

        heapq.heappush(maxq, minV*-1)
        heapq.heappush(minq, maxV)
    print(maxq[0]*-1)