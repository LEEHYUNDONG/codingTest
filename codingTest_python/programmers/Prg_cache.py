from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    for city in cities:
        if len(cache) == 0 or cacheSize == 0:
            answer += 5
            cache.append(city.lower())
        elif city.lower() in cache:
            answer += 1
            cache.remove(city.lower())
            cache.append(city.lower())
        elif city.lower() not in cache:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city.lower())
            elif len(cache) == cacheSize:
                cache.popleft()
                cache.append(city.lower())
            elif len(cache) == 0:
                cache.append(city.lower())

    return answer
