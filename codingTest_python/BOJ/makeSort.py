import heapq
import sys
input = sys.stdin.readline


n = int(input())
q = []
for _ in range(n):
    num = int(input())
    heapq.heappush(q, num)

while q:
    print(heapq.heappop(q))

