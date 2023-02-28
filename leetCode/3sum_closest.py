class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        clso = 10000000
        res = 0
        for ptr_1 in range(len(nums)-2):
            ptr_2, ptr_3 = ptr_1 + 1, len(nums)-1
            cur_target = target - nums[ptr_1]
            while ptr_2 < ptr_3:
                s = nums[ptr_2] + nums[ptr_3]
                if abs(cur_target - s) < clso:
                    clso = abs(cur_target - s)
                    res = s + nums[ptr_1]
                if cur_target < s:
                    ptr_3 -= 1
                elif cur_target > s:
                    ptr_2 += 1
                else:
                    return target
        return res
        