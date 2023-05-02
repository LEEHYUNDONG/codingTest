from bisect import bisect_left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        ans = []
            
        if start < len(nums) and nums[start] == target:
            ans.append(start)
            while start < len(nums) and nums[start] == target:
                start += 1
            ans.append(start-1)

            return ans
        
        return [-1, -1]