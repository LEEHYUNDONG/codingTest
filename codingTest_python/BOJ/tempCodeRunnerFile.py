import sys
from math import sqrt
input = sys.stdin.readline

N = int(input())


# 소수인지 판별하는 함수
def isPrime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

# 팰린드롬인지 판별하는 함수
def isPalindrome(num):
    numStr = list(str(num))
    stack = []
    size = len(numStr)
    # 3 // 2 -> 1, 6 // 2 -> 3
    # 12321 -> 1, 2 / 12344321
    for i in range(size//2):
        stack.append(numStr.pop())
    if size % 2:
        numStr.pop()
    
    while stack:
        if stack[-1] != numStr[-1]:
            return False
        stack.pop()
        numStr.pop()
    return True

MAXLENGTH = 1003002
if N == 1:
    print(2)
else:
    for i in range(N, MAXLENGTH):
        if isPrime(i) and isPalindrome(i):
            print(i)
            break
