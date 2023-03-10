class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        ans = ''
        for i in range(1, len(strs[0])):
            flag = True
            for j in range(1, len(strs)):
                if not strs[j].startswith(strs[0][0:i]):
                    flag = False
            if flag: 
                ans = strs[0][0:i]
        return ans