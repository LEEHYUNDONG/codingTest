import sys
input = sys.stdin.readline

n = int(input())
tmp = []
visited = [False]*n


def dfs(depth):
    global tmp
    if depth == n:
        for i in tmp:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if visited[i]:
            continue
        tmp.append(i+1)
        visited[i] = True
        dfs(depth+1)
        tmp.pop()
        visited[i] = False


dfs(0)
