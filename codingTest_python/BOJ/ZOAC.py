# s = input()
# visited = ['']*len(s)

# def dfs(s, idx, depth):
#     if depth == len(s):
#         return
#     minDist = int(1e9)
#     idx = -1
#     for i in range(len(s)-1, idx-1, -1):
#         if not visited[i] and minDist > abs(ord(s[i])-ord(prev)):
#             minDist = abs(ord(s[i])-ord(prev))
#             idx = i
#     if idx == -1:
#         idx = 0
#         for i in range(len(s)):
#             if not visited[i] and minDist > abs(ord(s[i])-ord(prev)):
#                 idx = i
#                 minDist = abs(ord(s[i])- ord(prev))
    
#     visited[idx] = True
#     for i in range(len(s)):
#         if visited[i]:
#             print(s[i], end = '')
#     print()
#     dfs(s, 'A', depth+1)


# dfs(s, min(s), 0)

s = input()
res = [""]*len(s)


def dfs(s, start):
    if not s:
        return
    minDist = int(1e9)
    idx = s.index(min(s))
    res[start+idx] = min(s)
    # print(''.join(res))
    print(res)
    dfs(s[idx+1:], start+idx+1)
    dfs(s[:idx], start)

dfs(s, 0)