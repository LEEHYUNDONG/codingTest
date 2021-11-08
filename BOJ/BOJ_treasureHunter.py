n, m, k = map(int, input().split())
treasure = [list(map(int, input().split())) for _ in range(k)]


graph = [[0]*m]*n
for x, y in treasure:
    graph[x-1][y-1] = 1


sort(treasure, key = lambda x : x[0])
