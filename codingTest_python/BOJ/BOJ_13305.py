n = int(input())
km = list(map(int, input().split()))
gas = list(map(int, input().split()))
mp = gas[0]
res = 0

for i in range(n-1):
    if gas[i] < mp:
        mp = gas[i]
    res += km[i]*mp
print(res)
