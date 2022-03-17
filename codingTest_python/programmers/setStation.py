import math


def solution(n, stations, w):
    answer = 0

    # 전파가 안통하는 구간의 (시작점, 끝점) 의 모음
    segments = []

    # 시작점 부터 시작 안테나 사이
    if stations[0] - w - 1 >= 1:
        segments.append([1, stations[0]-w-1])

    # 안테나 사이사이
    for i in range(len(stations) - 1):
        start = stations[i] + w + 1
        end = stations[i+1] - w - 1

        if start <= end:
            segments.append([start, end])

    # 끝 점까지
    if stations[-1] + w + 1 <= n:
        segments.append([stations[-1] + w + 1, n])

    print(segments)
    # 전파가 안통하는 구간 마다
    for segment in segments:
        # 구간의 길이
        length = segment[1] - segment[0] + 1

        if length <= w*2 + 1:
            answer += 1
        else:
            answer += math.ceil(length / (w*2 + 1))
    return answer
