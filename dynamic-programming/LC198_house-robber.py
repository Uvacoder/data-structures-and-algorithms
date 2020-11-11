class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic Programming Method:
        # Test case if list is empty or null
        if nums == None or len(nums) == 0:
            return 0
        
        # Test case if length of nums is only 1:
        if len(nums) == 1:
            return nums[0]
        
        # If the length of nums is more than 1:
        maxMoney = []
        maxMoney.append(nums[0])
        maxMoney.append(max(nums[0], nums[1]))
        
        
        for x in range(2, len(nums)):
            maxMoney.append(max(maxMoney[x-1], nums[x] + maxMoney[x-2]))

        return maxMoney.pop()
