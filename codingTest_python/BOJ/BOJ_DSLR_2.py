import sys
from collections import deque

input = sys.stdin.readline
t = int(input())


def bfs(start, end):
    visited = [0]*10000
    q = deque([[start, ""]])

    while q:
        num, op = q.popleft()
        if num == end:
            return op
        if not visited[num * 2 % 10000]:
            q.append([num*2 % 10000, op+"D"])
            visited[num*2 % 10000] = 1
        if not visited[(num - 1) % 10000]:
            q.append([(num-1) % 10000, op+"S"])
            visited[(num-1) % 10000] = 1
        if not visited[num % 1000*10+num//1000]:
            visited[num % 1000*10+num//1000] = True
            q.append([num % 1000*10+num//1000, op+"L"])
        if not visited[num % 10*1000+num//10]:
            visited[num % 10*1000+num//10] = True
            q.append([num % 10*1000+num//10, op+"R"])


for _ in range(t):
    s, e = map(int, input().split())
    print(bfs(s, e))

# print(1234 % 10)
# print(1234//10 + 1234 % 10 * 1000)
# print(1234 % 10)
