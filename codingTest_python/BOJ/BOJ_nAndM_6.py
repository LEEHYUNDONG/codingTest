import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = []
answer = []
visited = [False] * (n+1)


def dfs(idx, depth):
    # 방문했다면 리턴하는 것을 depth가 맞더라도 먼저 확인하게 해야한다.
    if visited[idx]:
        return
    if depth == m:
        ans.append(num[idx])
        for i in ans:
            print(i, end=' ')
        print()
        # 하나씩 pop 시켜놔야 방문하지 않았을 때 개수가 맞다.
        ans.pop()
        return
    for i in range(0, len(num)):
        if idx == i:
            continue
        ans.append(num[idx])
        visited[idx] = True
        dfs(i, depth+1)
        visited[idx] = False
        ans.pop()


num.sort()
for i in range(n):
    dfs(i, 1)
