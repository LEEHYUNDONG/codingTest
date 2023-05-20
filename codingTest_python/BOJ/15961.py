import sys
from collections import deque
input = sys.stdin.readline


n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = 0
right = 0
dict = {}
result = 0

while right < k:
    if arr[right] not in dict.keys():
        dict[arr[right]] = 0
    dict[arr[right]] += 1
    right += 1

if c not in dict.keys():
    dict[c] = 1
else:
    dict[c] += 1


while left < n:
    result = max(result, len(dict))
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0:
        del dict[arr[left]]
    if arr[right % n] not in dict.keys():
        dict[arr[right % n]] = 1
    else:
        dict[arr[right % n]] += 1
    left += 1
    right += 1


print(result)