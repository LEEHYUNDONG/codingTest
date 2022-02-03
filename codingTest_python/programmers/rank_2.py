from collections import defaultdict


def solution(n, results):
    answer = 0
    winner = defaultdict(set)
    loser = defaultdict(set)

    for i in results:
        w, l = i
        winner[l].add(w)
        loser[w].add(l)

    for i in range(1, n+1):
        for wins in winner[i]:
            loser[wins].update(loser[i])
        for loses in loser[i]:
            winner[loses].update(winner[i])

    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            answer += 1
    return answer
