cnt, answer = 0, 0


def dfs(w, s, target, depth):
    global answer, cnt
    if target == s:
        answer = cnt
        return
    if depth > 5:
        return
    cnt += 1
    for i in range(5):
        dfs(w, s + w[i], target, depth+1)


def solution(word):
    global answer
    w = ['A', 'E', 'I', 'O', 'U']
    dfs(w, '', word, 0)

    return answer
