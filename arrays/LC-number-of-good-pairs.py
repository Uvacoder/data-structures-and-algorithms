class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
#If we have k occerance of n, where n is number in nums array, then we can have k*(k-1)/2 good pairs.
#Keeping this in mind, and using set we can get following code.
#Using nC2 Logic
      count = 0 
      for x in set(nums):
        y = nums.count(x)
        count = count + int((y*(y-1)) / 2)
      
      return count
