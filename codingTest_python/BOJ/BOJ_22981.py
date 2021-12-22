n, k = map(int, input().split())
worktime = list(map(int, input().split()))
worktime.sort()

# if n == 2:
#     v = max(worktime) * (n-1) + worktime[-2]
#     print(int(k//v))
# else:
answer = float('inf')
for i in range(1, n):
    v = (worktime[0]*i) + (worktime[i]*(n-i))
    answer = min(answer, int(k//v) + (k%v != 0))
print(answer)
