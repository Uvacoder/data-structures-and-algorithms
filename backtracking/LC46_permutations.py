class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # back  tracking approach
        result = []
        
        
        if len(nums) == 1: 
            return [nums[:]]
        # we append a copy of stack rather than appending the stack itself.  Lists are mutable. So after appending a stack to our result, that stack will still be affected by any changes to its aliases (will be affected by all the opping and backtracking) 
                
        for x in range(len(nums)):
            n = nums.pop(0)
            stack = self.permute(nums)
            
            for perm in stack:
                perm.append(n)      # we want to append the first value we just removed (line 12) back into our stack
            result.extend(stack)    # add them to our result 
            nums.append(n)          # append the value we removed (line 12) back into nums
            
        return result
            
