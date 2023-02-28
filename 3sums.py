class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        ans = []
        for ptr1 in range(len(nums)-2):
            currTot = nums[ptr1]
            ptr2, ptr3 = ptr1 + 1, len(nums)-1
            while ptr2 < ptr3:
                s = nums[ptr2] + nums[ptr3]
                if s + currTot == 0 and [nums[ptr1], nums[ptr2], nums[ptr3]] not in ans:
                    ans.append([nums[ptr1], nums[ptr2], nums[ptr3]])
                
                if s + currTot < 0:
                    ptr2 += 1
                else:
                    ptr3 -= 1

        return ans