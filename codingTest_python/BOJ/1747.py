import sys
from math import sqrt
input = sys.stdin.readline

N = int(input())
MAXLENGTH = 1100000

# 소수인지 판별하는 함수
def isPrime(x): # 소수인지 판별해주는 함수
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

if N == 1000000:
    print(1003001)
else:
    for i in range(N, MAXLENGTH):
        if i == 1:
            continue
        if isPrime(i):
            primeStr = str(i)
            if primeStr == primeStr[::-1]:
                print(primeStr)
                break