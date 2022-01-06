
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
ans = []
res = 1000000


def dfs(depth):
    global ans
    global res
    if depth == n:
        t1, t2 = 0, 0
        for i in ans:
            print(i, end=' ')
        print()
        # for i in range(n-1):
        #     if i-1 == (n // 2):
        #         continue
        #     if i < n//2:
        #         t1 += graph[ans[i]][ans[i+1]] + graph[ans[i+1]][ans[i]]
        #     else:
        #         t2 += graph[ans[i]][ans[i+1]] + graph[ans[i+1]][ans[i]]
        # print("Power :", t1, t2)
        # res = min(res, abs(t1-t2))
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        dfs(depth+1)
        visited[i] = False
        ans.pop()


# 3 + 8 = 11
# 5 + 8 = 13
dfs(0)
print(res)
