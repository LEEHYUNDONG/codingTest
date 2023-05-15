class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))

'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1Lst = list(num1)
        n2Lst = list(num2)
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        pow1 ,pow2 = 0, 0
        realnum1, realnum2 = 0, 0

        while n1Lst:
            nt1 = int(n1Lst.pop(l1))
            realnum1 += ((10**pow1)*nt1)
            pow1 += 1
            l1-=1
        
        while n2Lst:
            nt2 = int(n2Lst.pop(l2))
            realnum2 += ((10**pow2)*nt2)
            pow2 += 1
            l2 -= 1
        
        
        return str(realnum1*realnum2)
        
'''