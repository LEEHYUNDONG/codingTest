n = int(input())
mat = list(map(int, input().split()))
m = int(input())
tarmat = list(map(int, input().split()))


def bin_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin_search(array, target, start, mid-1)
    else:
        return bin_search(array, target, mid+1, end)


mat.sort()
for t in tarmat:
    if bin_search(mat, t, 0, n-1) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
print()
