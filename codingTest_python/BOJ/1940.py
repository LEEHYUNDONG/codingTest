import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

l, r = 0, N-1
arr.sort()
cnt = 0


while l< r:
    if arr[l] + arr[r] == M:
        cnt += 1
    if arr[l] + arr[r] >= M:
        r -= 1
    else:
        l += 1
print(cnt)