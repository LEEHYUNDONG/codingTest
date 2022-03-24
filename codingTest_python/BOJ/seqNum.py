n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = -int(1e9)
tmp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    tmp[i] = arr[i-1] + tmp[i-1]


for i in range(n-m+1):    
    ans = max(tmp[i+m]-tmp[i], ans)
    
print(ans)