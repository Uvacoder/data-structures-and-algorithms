class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        You must do this in-place without making a copy of the array.
        """
        #two pointer approach
        
        # Count the zeros
        numOfZeros = 0
        for x in nums:
            if x == 0:
                numOfZeros += 1
                
        # Same method as in LC27
        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1
        
        if numOfZeros == 1:
            nums[-numOfZeros] = 0
        elif numOfZeros != 0: 
            for w in range(1, numOfZeros + 1):
                nums[-w] = 0

########################################################################            
        # Much cleaner version of the two pointer appraoch
        # Slow pointer = i
        # Faster pointer is the for loop.  Does the job of processing new elements
        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1
        for w in range(i, len(nums)):
            nums[w] = 0
