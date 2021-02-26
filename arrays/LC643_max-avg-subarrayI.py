class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # goal is to find the highest average value in the array 
        # with 'k' being the amount of integers you can add
        sum = 0
        
        
        # get the sum of elements from index 'x' to index 'x + k' and we put the result in 'sum'
        for x in range(k):
            sum = sum + nums[x]
            
        # assume we already know the sum of elements from index 'x' to index 'x+k', and we put that into 'sum'
        # to find the sum from index "x + 1" to the index "x+k+1", we need to subtract elements nums[x] from sum and add element nums[x+k+1] to sum
        result = sum
        for x in range(k, len(nums) ):
            sum = sum + nums[x] - nums[x-k]
            result = max(result, sum)
            
        return result / k
