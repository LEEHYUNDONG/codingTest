import math


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    num = ''
    while n:  # 소수 구하는 파트
        num += str(n % k)
        n = n // k
    num = num[::-1]
    # 문자열 부분으로 나누는 파트
    num = num.replace('0', ' ')
    print(num)
    for i in num.split():
        if isPrime(int(i)):
            answer += 1

    return answer
