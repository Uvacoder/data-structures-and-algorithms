class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        # Appraoch 3: Caching
        self.sumArray = [0] 
        for x in range(len(nums)):
            self.sumArray.append(self.sumArray[x] + nums[x])

    def sumRange(self, i: int, j: int) -> int:
        # Approach 1: Brute Force
            # sum = 0
            # for x in range(i,j+1):
            #     sum += self.nums[x] 
            # return sum
        
        # Approach 3: Caching
        # https://www.youtube.com/watch?v=CjPMfq3ULZg
        return self.sumArray[j+1] - self.sumArray[i]
        
        

    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
