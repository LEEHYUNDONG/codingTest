N, M = map(int, input().split())

f = [0 for _ in range(N+1)]

def factorial(n):
    if n == 1:
        return 1
    f[n] = n*factorial(n-1)
    return f[n]

factorial(N)
print((f[N]//(f[N-M]*f[M])))