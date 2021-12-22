import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, end):
    q = deque([[start, ""]])
    visited = [0] * 10000
    visited[start] = True

    while q:
        num, op = q.popleft()

        if num == end:
            return op
        if not visited[num*2 % 10000]:
            visited[num*2 % 10000] = True
            q.append([num*2 % 10000, op + "D"])
        if not visited[(num-1) % 10000]:
            visited[(num-1) % 10000] = True
            q.append([(num-1) % 10000, op+"S"])
        if not visited[num % 1000*10+num//1000]:
            visited[num % 1000*10+num//1000] = True
            q.append([num % 1000*10+num//1000, op+"L"])
        if not visited[num % 10*1000+num//10]:
            visited[num % 10*1000+num//10] = True
            q.append([num % 10*1000+num//10, op+"R"])


t = int(input())

for _ in range(t):
    x,  y = map(int, input().rsplit())
    print(bfs(x, y))
