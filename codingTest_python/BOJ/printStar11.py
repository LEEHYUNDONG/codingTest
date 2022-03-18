# import sys
# sys.setrecursionlimit(10**6)

n = int(input())
graph = [[' ']*2*n for _ in range(n)]

def printStar(x, y, l):
    if l == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = graph[x+1][y+1] = '*'
        for i in range(-2, 3):
            graph[x+2][y+i] = '*'
    else:
        d = l // 2
        printStar(x, y, d)
        printStar(x+d, y-d, d)
        printStar(x+d, y+d, d)

printStar(0, n-1, n)

for i in graph:
    print(''.join(i))