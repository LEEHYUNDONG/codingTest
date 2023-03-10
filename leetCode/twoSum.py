class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[n] = idx
