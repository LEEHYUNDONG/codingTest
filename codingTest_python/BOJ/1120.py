import sys
input = sys.stdin.readline

A, B = input().rsplit()
cnt = len(B)


def dfs(A, B, start, end):
    global cnt
    if start+len(A) > len(B):
        return
    d = 0
    for i in range(len(A)):
        if A[i] != B[i+start]:
            d+=1
    cnt = min(d, cnt)
    dfs(A, B, start+1, end)

dfs(A, B, 0, len(B))
print(cnt)