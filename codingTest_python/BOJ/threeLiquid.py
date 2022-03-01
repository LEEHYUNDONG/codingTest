import sys

n = int(input())
liq = list(map(int, input().split()))

liq.sort()
ans = 0
minL = sys.maxsize

for i in range(n-2):
    l = i + 1
    r = n - 1
    while l < r:
        tot = liq[i] + liq[l] + liq[r]
        if abs(tot) < minL:
            minL = abs(tot)
            ans = [liq[i], liq[l], liq[r]]
        if tot < 0:
            l += 1
        elif tot > 0:
            r -= 1
        else:
            break

print(ans[0], ans[1], ans[2])