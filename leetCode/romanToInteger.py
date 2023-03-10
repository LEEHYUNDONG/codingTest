class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {
            'I' : 1
            ,'V' : 5
            ,'X' : 10
            ,'L' : 50
            , 'C' : 100
            ,'D' : 500
            ,'M' : 1000
        }

        ans = 0
        for i in range(len(s)):
            if i+1 < len(s) and romanDic[s[i]] < romanDic[s[i+1]]:
                ans -= romanDic[s[i]]
            else:
                ans += romanDic[s[i]]
            
        
        return ans
