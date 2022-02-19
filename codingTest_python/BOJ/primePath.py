import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

answer = []
test_case = []

for _ in range(t):
    n, m = map(int, input().split())
    test_case.append([n, m])

arr = [0] * (10000)

for i in range(10000):
    arr[i] = i

arr[1] = 0

for i in range(2, 10000):
    if arr[i] == 0:
        continue
    for j in range(i*i, 10000, i):
        arr[j] = 0


ans = 0
def bfs(start, target):
    q = deque()
    q.append([start, 0])

    # 방문여부
    visited = [0 for i in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        strNow = str(now)

        if now == target:
            return cnt

        for i in range(4):

            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                if visited[temp] == 0 and arr[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])


for i in test_case:
    start, target = i[0], i[1]
    ans = bfs(start, target)
    if ans == None:
        answer.append("Impossible")
    else:
        answer.append(ans)

for i in answer:
    print(i)
