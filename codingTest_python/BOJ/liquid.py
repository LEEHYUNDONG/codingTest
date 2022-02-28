import sys
input = sys.stdin.readline

n = int(input())
l, r = 0, n-1
liq = list(map(int, input().split()))

tot = 2147483647
ans = 0
while l < r:
    if tot >= abs(liq[l]+liq[r]):
        ans = [liq[l], liq[r]]
        tot = abs(liq[l]+liq[r])
    if liq[l] + liq[r] < 0:
        l += 1
    else:
        r -= 1

print(ans[0], ans[1])