import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return array.count(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

T = int(input())


for _ in range(T):
    N = int(input())
    arr = set(map(int, input().split()))
    M = int(input())
    targets = list(map(int, input().split()))

    val = {}
    for target in arr:
        if target not in val.keys():
            val[target] = True
    
    for target in targets:
        if target not in val.keys():
            print(0)
        else:
            print(1)
