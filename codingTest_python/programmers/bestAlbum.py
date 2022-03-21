from collections import deque
import heapq


def solution(genres, plays):
    answer = []
    played = dict()
    gen = dict()

    for i in range(len(genres)):
        if genres[i] not in played.keys():
            played[genres[i]] = 0
            played[genres[i]] += plays[i]
            gen[genres[i]] = [[i, plays[i]]]
            continue
        played[genres[i]] += plays[i]
        gen[genres[i]].append([i, plays[i]])

    for (k, v) in sorted(played.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(gen[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
