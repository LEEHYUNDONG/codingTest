def bin_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # 중간 점보다 찾고자하는 target 값이 작은 경우 왼쪽 탐색
    elif array[mid] > target:
        return bin_search(array, target, start, mid-1)
    # 중간 점보다 찾고자하는 값이 큰 경우 오른쪽 탐색
    else:
        return bin_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = bin_search(array, target, 0, n-1)

if result == None:
    print("답 없다~ 마치 우리 인생~")
else:
    print(result + 1)
