import sys
input = sys.stdin.readline
n = int(input())


def dfs(num, target):
    global ans
    if num == target:
        ans += 1
        return
    if num > target:
        return
    dfs(num+1, target)
    dfs(num+2, target)
    dfs(num+3, target)
    return ans


ans = 0
answer = []
for i in range(n):
    ans = 0
    target = int(input())
    answer.append(dfs(0, target))

for i in answer:
    print(i)
