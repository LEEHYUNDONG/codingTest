import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = []
answer = []
visited = [False] * (n+1)


def dfs(idx, depth):
    if depth == m:
        ans.append(num[idx])
        for i in ans:
            print(i, end=' ')
        print()
        # 하나씩 pop 시켜놔야 방문하지 않았을 때 개수가 맞다.
        ans.pop()
        return
    for i in range(0, len(num)):
        ans.append(num[idx])
        dfs(i, depth+1)
        ans.pop()


num.sort()
for i in range(n):
    dfs(i, 1)
