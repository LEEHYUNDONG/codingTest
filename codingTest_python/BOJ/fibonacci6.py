import sys
sys.setrecursionlimit(10**6)
N = int(input())
arr = [0 for _ in range(N+1)]

arr[1] = 1

def fib(n):
    if n == 0 or n == 1:
        return arr[n]
    arr[n] = (fib(n-1) + fib(n-2)) %1000000007
    return arr[n]%1000000007

fib(N)
print(arr[N])