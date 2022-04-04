def solution(n, times):
    answer = 0
    l, r = 1, max(times)*n
    mid = (l+r)//2

    while l <= r:
        mid = (l+r)//2
        people = 0
        for i in times:
            people += mid // i

        if people < n:
            l = mid + 1
        elif people >= n:
            r = mid - 1

        answer = l

    return answer
