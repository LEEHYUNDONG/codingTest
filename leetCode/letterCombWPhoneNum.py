class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterDic = {
            '2': ['a', 'b', 'c']
            ,'3' : ['d', 'e', 'f']
            ,'4' : ['g', 'h', 'i']
            ,'5' : ['j', 'k', 'l']
            ,'6' : ['m', 'n', 'o']
            ,'7' : ['p', 'q', 'r', 's']
            ,'8' : ['t', 'u', 'v']
            ,'9' : ['w', 'x', 'y', 'z']
        }
                
        def dfs(idx, comb):
            if len(comb) == len(digits):
                ans.append(comb)
                return
            for i in range(len(letterDic[digits[idx]])):
                dfs(idx+1, comb+letterDic[digits[idx]][i])

        ans = []
        dfs(0, '')

        if digits == "":
            return []

        return ans