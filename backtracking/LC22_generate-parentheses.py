class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Checks for 3 required agendas
        # only add right if right < left 
        # if right == left == n, return
        # if left < n, add parentheses
        
        # back tracking approach
        stack = []
        result = []
        
        def backtracking(left, right):
            if left == right == n:
                print("before join: ", result)
                result.append("".join(stack))
                print("after join: ", result)
                return
            
            if left < n:
                stack.append("(")
                backtracking(left + 1, right)
                stack.pop()
            
            if right < left:
                stack.append(")")
                backtracking(left, right + 1)
                stack.pop()
        
        backtracking(0, 0)
        return result


