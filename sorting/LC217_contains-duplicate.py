class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) != len(set(nums)):
        #     return True 
        # else:
        #     return False 
        
        # Approach 3: Hash Table
        mySet = set() 
        
        for x in nums:
            if x not in mySet:
                mySet.add(x)
            else:
                return True
        return False
