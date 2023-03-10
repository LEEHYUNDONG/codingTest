class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = 100000
        l, r = 0, len(height)
        ans = 0
        while l < r:
            h = min(height[l], height[r])
            ans = max((l-r)*h, ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
            
