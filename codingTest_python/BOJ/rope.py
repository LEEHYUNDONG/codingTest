n = int(input())

ans = -1
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)

for i in range(n):
    if ans < rope[i]*(i+1):
        ans = rope[i]*(i+1)
print(ans)
