import sys
input = sys.stdin.readline

N, k = map(int, input().split())
arr = list(map(int, input().split()))
tot, ans = 0, 0


for i in range(N+k):
    tot += arr[i%N]
    if i > k-1:
        tot -= arr[(i-k)%N]
    ans = max(tot, ans)

print(ans)