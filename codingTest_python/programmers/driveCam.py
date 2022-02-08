def solution(routes):
    answer = 0
    routes.sort()
    i = 0
    cnt = 0
    while routes:
        tmp = 0
        prev, cur = routes[0][0], routes[0][-1]
        for i in range(1, len(routes)):
            if prev <= routes[i][0] <= cur and prev <= routes[i][1] <= cur:
                prev = routes[i][0]
                cur = routes[i][1]
            elif prev <= routes[i][0] <= cur:
                prev = routes[i][0]
            elif routes[i][1] <= cur:
                cur = routes[i][1]
            elif cur < routes[0][-1] or prev > routes[0][0]:
                break
        for k in routes:
            a, b = k
            if a <= prev <= b:
                tmp += 1
        for _ in range(tmp):
            if routes != []:
                routes.pop(0)
        answer += 1

    return answer
