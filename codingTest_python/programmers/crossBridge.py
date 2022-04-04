def solution(distance, rocks, n):
    answer = 0
    l, r = 0, distance
    rocks.sort()

    while l <= r:
        mid = (l+r)//2
        cnt = 0
        prev = 0
        minV = int(1e9)

        for i in rocks:
            if i - prev < mid:
                cnt += 1
            else:
                prev = i
            if cnt > n:
                break
        # print(l, r)
        if cnt > n:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid

    return answer
