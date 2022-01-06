import sys
input = sys.stdin.readline

n = int(input())
sign = list(input().split())
# num = [i for i in range(10)]
visited = [False] * 10
res = []
ans = []


def check(num):
    for i in range(len(sign)):
        if sign[i] == '<':
            if int(num[i]) >= int(num[i+1]):
                return False
        elif sign[i] == '>':
            if int(num[i]) < int(num[i+1]):
                return False
    return True


def dfs(idx, depth):
    global res, ans
    if depth == n+1 and check(res):
        ans.append(''.join(res))
        return
    for i in range(10):
        if visited[i]:
            continue
        visited[i] = True
        res.append(str(i))
        dfs(i, depth+1)
        res.pop()
        visited[i] = False


dfs(0, 0)
print(ans[-1])
print(ans[0])
