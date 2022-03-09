import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    graph = []
    

    for _ in range(2):
        graph.append(list(map(int, input().split())))
    
    for i in range(1, n):
        if i == 1:
            graph[0][i] += graph[1][i-1]
            graph[1][i] += graph[0][i-1]
            continue
        graph[0][i] += max(graph[1][i-1], graph[1][i-2])
        graph[1][i] += max(graph[0][i-1], graph[0][i-2])
    
    ans.append(max(graph[0][-1], graph[1][-1]))

for i in ans:
    print(i)