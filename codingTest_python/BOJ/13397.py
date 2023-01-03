import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, max(arr)
ans = 0


def divide(x):
    max_x=min_x=arr[0]
    cnt=1
    for i in range(1,N):
        max_x=max(max_x,arr[i])
        min_x=min(min_x,arr[i])
        if max_x - min_x > x:
            cnt+=1
            max_x=arr[i]
            min_x=arr[i]
    return cnt


while l <= r:
    mid = (l+r) // 2
    if divide(mid) <= M:
        r = mid - 1
        ans = mid
    else:
        l = mid +1

print(ans)