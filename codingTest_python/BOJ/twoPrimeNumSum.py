import sys
input = sys.stdin.readline

num = int(input())
arr = [i for i in range(num+1)]


def primeNum(num):
    for i in range(2, num+1):
        if arr[i] == 0:
            continue
        for j in range(i+i, num+1, i):
            arr[j] = 0

primeNum(num)
prime = []

for i in range(2, num+1):
    if arr[i] != 0:
        prime.append(arr[i])

l, r = 0, 0
tot = 0
ans = 0

while l <= r:
    if tot == num:
        ans += 1
    if tot > num:
        tot -= prime[l]
        l += 1
    elif r == len(prime):
        break
    else:
        tot += prime[r]
        r += 1

print(ans)
