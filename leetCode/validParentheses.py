class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = list(s)
        stack2 = []
        
        while stack1:
            tmp = stack1[-1]
            stack1.pop()
            if tmp == ')' or tmp == ']' or tmp == '}':
                stack2.append(tmp)
            elif stack2 and tmp =='(' and stack2[-1] == ')':
                stack2.pop()
        
            elif stack2 and tmp =='[' and stack2[-1] == ']':
                stack2.pop()
                
            elif stack2 and tmp == '{' and stack2[-1] == '}':
                stack2.pop()
                
            else:
                return False
            
        if stack2:
            return False
        return True