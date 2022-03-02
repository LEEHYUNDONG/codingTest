import sys
input = sys.stdin.readline

N, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def power(M, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                
                M[i][j] %= 1000
        return M
    
    tmp = power(M, n//2)
    res = matMul(tmp, tmp)
    if n % 2 == 0:
        return res
    else:
        return matMul(M, res)

def matMul(A, B):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= 1000
    return C

res = power(A, b)

for q in range(N):
    print(*res[q])            
