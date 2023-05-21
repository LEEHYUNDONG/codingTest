import sys
from collections import defaultdict
input = sys.stdin.readline


n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left = 0
right = 0
dict = defaultdict(int)
result = 0

while right < k:
    if arr[right] not in dict.keys():
        dict[arr[right]] = 0
    dict[arr[right]] += 1
    right += 1


dict[c] += 1


while left < n:
    result = max(result, len(dict))
    dict[arr[left]] -= 1
    if dict[arr[left]] == 0:
        del dict[arr[left]]
    dict[arr[right % n]] += 1
    left += 1
    right += 1


print(result)