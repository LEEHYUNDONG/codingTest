def solution(n, times):
    answer = 0
    l, r = 1, max(times)*n
    mid = (l+r)//2

    while l <= r:
        time = 0
        mid = (l+r)//2
        for i in times:
            time += mid // i
        if time >= n:
            r = mid - 1
        elif time < n:
            l = mid + 1
        answer = l

    return answer
