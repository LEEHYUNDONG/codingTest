import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

arr.sort()
count = {}
for a in arr:
    if a not in count:
        count[a] = 1
    count[a] += 1


def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if array[mid] == target:
        return count.get(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for target in targets:
    print(binary_search(arr, target, 0, N-1), end = ' ')
