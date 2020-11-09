class Solution:
    def isValid(self, s: str) -> bool:
        
# Approach 1: Stacks
      # Approach 1: Stacks
      # Check if it's an open statement ({[, if yes append it into the list
      # if the list is contains a character AND current character is }]) AND the last character is list is {[( take it out of the list
        myStack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                myStack.append(x)
            elif myStack and x == ')' and myStack[-1] == '(':
                myStack.pop()
            elif myStack and x == ']' and myStack[-1] == '[':
                myStack.pop()
            elif myStack and x == '}' and myStack[-1] == '{':
                myStack.pop()
            else: 
                return False
            
        if not myStack:
            return True
        else:
            return False


