import sys
input = sys.stdin.readline

target = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split())
A.sort()
B.sort()
ans = 0

# A 탐색
for i in range(N):
    # B를 탐색하여 경우의 수 계산
    
