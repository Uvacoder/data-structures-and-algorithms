class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1: sorting
        nums.sort()
        n = len(nums)
        
        if nums[-1] != n:
            return n 
        elif nums[0] != 0:
            return 0
        
        for x in range(1, n):
            expected_num = nums[x-1] + 1
            if nums[x] != expected_num:
                return expected_num
        
        # My approach: long runtime
        # n = len(nums)
        # for x in range(0,n+1):
        #     if x not in nums:
        #         return x
