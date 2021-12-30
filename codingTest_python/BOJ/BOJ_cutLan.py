import sys
input = sys.stdin.readline
n, k = map(int, input().split())
lan = [int(input()) for _ in range(n)]
l, r = 1, max(lan)

while l <= r:
    mid = (l+r) // 2
    num = 0
    for i in lan:
        num += (i // mid)
    if num >= k:
        l = mid + 1
    else:
        r = mid - 1

print(r)
