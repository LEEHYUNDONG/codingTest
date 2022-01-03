from bisect import bisect_left, bisect_right
arr = [-1, -2, -3, 42, 4, 10, -33, -10, 30, 40, 60, 70]
arr.sort()

print(arr[bisect_left(arr, -2):])  # -2를 포함 오른쪽 나머지 배열 출력
print(len(arr) - bisect_left(arr, -2))  # -2 를 포함하여 큰 숫자들의 개수

print(arr[bisect_right(arr, -2):])  # -2를 제외하고 오른쪽 나머지 배열 출력
print(len(arr) - bisect_right(arr, -2))  # -2보다 큰 수들
