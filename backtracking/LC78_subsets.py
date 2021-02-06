class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # back tracking approach
        def backtrack(input_nums, index, tempArray, result):
            if len(tempArray) > len(nums):
                return
            
            result.append(list(tempArray))
            
            for x in range( index, len(input_nums) ):
                tempArray.append(input_nums[x])
                backtrack(input_nums, x + 1, tempArray, result)
                tempArray.pop()
            
        result = []
        backtrack(nums, 0, [], result)
        return result
