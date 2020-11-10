class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach 3: Dynamic Programming
        if n <= 3:
            return n
        
        stackForNumberOfWays = [0, 1, 2, 3]
        for x in range(4,n+1):
            stackForNumberOfWays.append(stackForNumberOfWays[x-1] + stackForNumberOfWays[x-2])
            
        return stackForNumberOfWays.pop()
