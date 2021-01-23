class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        
        for x in range(len(S)):
            try: 
                if S[x] == '#':
                    stack1.pop()
                else:
                    stack1.append(S[x])
            except IndexError:
                pass
            
        for x in range(len(T)):
            try:
                if T[x] == "#":
                    stack2.pop()
                else:
                    stack2.append(T[x])
            except IndexError:
                pass
                
        if stack1 == stack2:
            return True
        else:
            return False
