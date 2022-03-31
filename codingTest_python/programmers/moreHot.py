import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)

    while scoville:
        x = heapq.heappop(scoville)
        if len(scoville) == 0 and x < K:
            return -1

        if len(scoville) >= 1 and x < K:
            Sx = heapq.heappop(scoville)
            tmp = Sx*2 + x
            scoville.append(tmp)
            answer += 1

    return answer
