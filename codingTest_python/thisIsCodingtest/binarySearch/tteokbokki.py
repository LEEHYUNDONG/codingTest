n, m = map(int, input().split())
tteok = list(map(int, input().split()))

start, end = 0, max(tteok)
mid = 0
flag = False

while start < end:
    mid = (start + end)//2
    tot = 0
    for i in tteok:
        if (i-mid) < 0:
            continue
        else:
            tot += (i-mid)

    if tot == m:
        flag = True
        break
    elif tot > m:
        start = mid + 1
    else:
        end = mid - 1

if flag:
    print(mid)
