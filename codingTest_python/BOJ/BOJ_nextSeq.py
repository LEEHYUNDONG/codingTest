import sys
input = sys.stdin.readline

n = int(input())
fin = list(map(int, input().split()))
flag = False
visited = [False] * (n+1)


def dfs(num, depth):
    global flag
    if depth == n:
        if flag:
            for i in num:
                print(i, end=' ')
            print()
            flag = False
            return
        if fin == num:
            flag = True
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        num.append(i)
        dfs(num, depth+1)
        visited[i] = False
        num.pop()


dfs([], 0)
if flag:
    print(-1)
