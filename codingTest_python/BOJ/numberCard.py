import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


m = int(input())
ans = []
tmp = list(map(int, input().split()))

for i in tmp:
    if binary_search(num, i, 0, n-1) is not None:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)