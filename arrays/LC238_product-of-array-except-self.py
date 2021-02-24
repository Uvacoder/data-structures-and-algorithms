class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach 1: left and right product lists
        length = len(nums)
        left = [0] * length
        right = [0] * length
        output = []
        
        left[0] = 1
        for x in range(1, length):
            left[x] = left[x-1] * nums[x-1]
            
        right[-1] = 1 
        for x in range(length-2, -1, -1):
            right[x] = right[x+1] * nums[x+1]
            
        for x in range(length):
            output.append(left[x] * right[x])
        
        return output
            
        # # my way: brute force!
        # left = 0
        # right = len(nums) - 1
        # current = 0
        # output = []
        # repititions = len(nums)
        # 
        # while repititions > 0:
        #     result = 1
        #     for x in range(len(nums)):
        #         if x == current:
        #             continue
        #         result = result * nums[x]
        #     output.append(result) 
        #     current += 1 
        #     repititions -= 1  
        #     
        # return output 
        
