import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

l, r = 0, 0
arr.sort() #정렬해야함.
ans = max(arr) - min(arr)
dp = [0 for _ in range(N)]

# 커서가 왼쪽과 오른쪽이 같이 시작한다
while l <= r and r < N:
    
    if arr[r] - arr[l] >= M:
        ans = min(ans, arr[r]-arr[l])
        l += 1
    else:
        r += 1
print(ans)