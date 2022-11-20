import sys
input = sys.stdin.readline


N, k, m = map(int, input().split())

cnt = 0

while k != m:
    k -= k//2
    m -= m//2
    cnt +=1

print(cnt)