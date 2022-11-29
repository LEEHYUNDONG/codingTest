import sys
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))
hugeso = list(map(int, input().split()))

hugeso.sort()
print(*hugeso)
