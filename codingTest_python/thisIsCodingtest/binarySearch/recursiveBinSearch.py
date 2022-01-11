def bin_search(target, start, end, array):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return bin_search(target, start, mid-1, array)
    else:
        return bin_search(target, mid+1, end, array)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = bin_search(target, 0, n-1, array)
if result == None:
    print("원소 없다")
else:
    print(result+1)
