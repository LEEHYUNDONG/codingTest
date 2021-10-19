from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        p = 0  # window left border
        dic = {}
        for c in s:
            dic[c] = -1
        for i in range(len(s)):  # i is the left border of the window
            if dic[s[i]] >= p:  # checking if the "last seen" character is in the window
                p = dic[s[i]]+1
            dic[s[i]] = i # update the "last seen" characters index
            if i - p+1 > count:
                count = i-p+1
        return count
