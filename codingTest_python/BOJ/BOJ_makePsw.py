import sys
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
ans = []
visited = [False] * c


def checkPassword(ps):
    wc = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in wc:
        if i in ps:
            cnt += 1

    if len(ps)//2 < cnt or cnt == 0:
        return False
    else:
        return True


def dfs(idx, word, depth):
    if depth == l and checkPassword(word):
        global ans
        ans.append(word)
        return

    for i in range(idx, c):
        if visited[i]:
            continue
        visited[i] = True
        dfs(i, word + alpha[i], depth+1)
        visited[i] = False


dfs(0, '', 0)
for i in ans:
    print(i)
