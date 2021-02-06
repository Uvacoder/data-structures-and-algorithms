class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # two pointer appraoch
        summary_range = []
        a = 0
        b = 1    # this will be our fast pointer
        lenNums = len(nums) 
        
        if lenNums == 0:
            return []
        
        
        summary_range = [ str(nums[0]) ]    # adds the beginning of the range
        while a < lenNums and b < lenNums:
            if nums[b] - nums[a] == 1:  # if they subtract to 1 that means they are in order
                b += 1
                a += 1
            else:
                if summary_range[-1] != str(nums[a]):
                    summary_range[-1] = summary_range[-1] + "->" + str(nums[a])
                
                a = b
                summary_range.append( str(nums[a]) )     # adds teh beginning of the range
                b += 1
        
        
        if summary_range[-1] != str(nums[a]):
            summary_range[-1] = summary_range[-1] + "->" + str(nums[a])
            
        return summary_range
