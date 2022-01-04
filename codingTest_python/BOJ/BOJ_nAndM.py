import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [i for i in range(1, n+1)]


def dfs(num, tmp, depth):
    if depth == m:
        tmp.append(num)
        for i in tmp:
            print(i, end=' ')
        print()
        tmp.pop()
        return
    for i in range(num, n+1):
        tmp.append(num)
        dfs(i, tmp, depth+1)
        tmp.pop()


for i in range(1, n+1):
    tmp = []
    dfs(i, tmp, 1)
