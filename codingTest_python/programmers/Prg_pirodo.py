answer = -1


def dfs(idx, dungeons, visited,  pro, depth):
    global answer
    answer = max(depth, answer)
    for i in range(len(dungeons)):
        if not visited[i] and pro >= dungeons[i][0]:
            visited[i] = True
            dfs(i, dungeons, visited, pro-dungeons[i][1], depth+1)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(0, dungeons, visited, k, 0)
    return answer
