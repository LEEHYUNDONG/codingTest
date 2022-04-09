N = int(input())
lines = list(map(int, input().split()))

loc = [-1 for _ in range(N)]

for height, left in enumerate(lines):
    cnt = 0
    for i in range(N):
        if cnt == left and loc[i] == -1:
            loc[i] = height+1
            break
        elif loc[i] == -1:
            cnt += 1


print(*loc)