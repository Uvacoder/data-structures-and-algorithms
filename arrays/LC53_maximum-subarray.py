# this problem is also found in the 'dynamic-programming' directory

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dynamic programming approach
        largest_sum = nums[0] 
        current = nums[0]
        
        for x in nums[1:]:  # start from 1st index 
            current = max(x, current + x)  # finding the biggest sum
            
            if current > largest_sum:
                largest_sum = current
            
        return largest_sum 
