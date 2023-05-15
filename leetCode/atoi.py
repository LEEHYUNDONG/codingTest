class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        s = s.strip()
        flag = False
        
        for i in s:
            if i.isdigit():
                n = ord(i) - ord('0')
                ans = ans*10 + int(i)
                flag = True
            elif not flag and (i == '-' or i == '+'):
                flag = True
                continue
            else:
                break
                
        if s == "":
            return 0
        if s[0] == '-':
            ans *= -1
        
        if ans > 2**31 - 1:
            return 2**31 - 1
        elif ans < -2**31:
            return -2**31
        return ans
