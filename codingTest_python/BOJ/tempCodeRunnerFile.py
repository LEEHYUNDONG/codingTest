import sys
input = sys.stdin.readline

N, M, L = list(map(int, input().split()))
hugeso = [0] + list(map(int, input().split())) + [L]

hugeso.sort()

l, r = 1, L - 1
ans = 0

while l <= r:
    count = 0
    mid = (l+r) // 2
    for i in range(1, len(hugeso)):
        if hugeso[i] - hugeso[i-1] > mid:
            count += (hugeso[i]-hugeso[i-1]-1)//mid
    if count > M:
        l = mid + 1
    else:
        r = mid - 1
        ans = mid

print(ans)