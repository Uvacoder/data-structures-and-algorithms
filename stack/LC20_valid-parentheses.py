# you can find this same problem in my 'strings' directory

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == '[' or x == '{' or x == '(':
                stack.append(x)
            
            # if stack is NOT empty and the brackets match each other
            elif stack and x == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and x == '}' and stack[-1] == '{':
                stack.pop()
                print(stack)
            elif stack and x == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        if not stack:  # if stack is empty
            return True
        else:
            return False
