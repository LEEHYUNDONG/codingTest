import sys
x, y = map(int, input().split())
win = y*100//x
ans = sys.maxsize

l, r = 1, x
while l <= r:
    mid = (l+r)//2
    tmp = (y+mid)*100 //(x+mid)

    if tmp > win:
        ans = min(mid, ans)
        r = mid - 1
    else:
        l = mid + 1

print(ans) if ans != sys.maxsize else print(-1)