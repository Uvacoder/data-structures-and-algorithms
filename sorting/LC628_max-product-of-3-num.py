class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        output = 1
        if len(nums) <= 3:
            for x in nums:
                output = output * x
            return output
        
        # the product of the last 3 values
        output2 = 1
        for x in (nums[-3:]):
            output2 *= x
                
        # the product of the first 2 values and the last value
        output3 = 1
        for x in (nums[:2]):
            output3 *= x
        output3 *= nums[-1]
        
        return max(output2, output3) 
