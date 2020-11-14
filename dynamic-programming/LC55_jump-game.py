class Solution:
    def canJump(self, nums: List[int]) -> bool:
# Approach 4: Greedy  
        leftMostIndex = len(nums) - 1
        #print(leftMostIndex)
        
        for x in range(len(nums) , 0, -1):
            #print("This is the index: ",x-1)
            #print("This is the addition: ", nums[x-1] + (x-1), '\n')
            if nums[x-1] + (x-1) >= leftMostIndex:
                leftMostIndex = x - 1
                #print("This is leftMostIndex: ", leftMostIndex, '\n')

        return leftMostIndex == 0
