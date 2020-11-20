class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
# Approach 3: my version of Dynamic Programming
        longestIncrease = [1] * len(nums)
        
        for j in range(1, len(nums)  ):
            for i in range(len(nums)): 
                if i >= j:
                    break
                if nums[j] > nums[i]:
                    longestIncrease[j] = max(longestIncrease[i] + 1, longestIncrease[j])
                        
        return max(longestIncrease)
