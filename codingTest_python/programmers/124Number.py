def solution(n):
    answer = ''
    numDic = {1: '1', 2: '2', 0: '4'}
    tmp = n

    while n > 0:
        answer += numDic[n % 3]
        if n % 3 == 0:
            n -= 1
        n = n // 3

    return answer[::-1]
