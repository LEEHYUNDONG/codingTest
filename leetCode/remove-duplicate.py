class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst = defaultdict(int)
        idx = 0

        for i in nums:
            if lst[i] == 0:
                lst[i] += 1
                nums[idx] = i
                idx += 1

        
        
        return idx