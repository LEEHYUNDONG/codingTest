import copy
answer = -int(1e9)


def solution(info, edges):
    global answer
    graph = [[]*len(info) for _ in range(len(info))]

    for a, b in edges:
        graph[a].append(b)

    def dfs(start, sheep, wolf, tmp):
        global answer
        if info[start] == 0:
            sheep += 1
        else:
            wolf += 1

        if sheep <= wolf:
            return

        answer = max(sheep, answer)

        for s in tmp:
            for i in graph[s]:
                if i not in tmp:
                    tmp.append(i)
                    dfs(i, sheep, wolf, tmp)
                    tmp.pop()

    dfs(0, 0, 0, [0])

    return answer
