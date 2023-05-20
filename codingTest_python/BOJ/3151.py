import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0

for i, n in enumerate(nums):
    l, r = i + 1, N-1
    while l<r:
        s = nums[l] + nums[r] + nums[i]
        if s > 0:
            r -= 1
        else:
            if s == 0:
                if nums[l] == nums[r]:
                    cnt += r - l
                else:
                    tmp = bisect_left(nums, nums[r])
                    cnt += r - tmp + 1
            l += 1
print(cnt)
