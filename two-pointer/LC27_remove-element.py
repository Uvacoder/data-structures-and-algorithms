class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer approach
        i = 0
        
        for x in range(len(nums)):
            if nums[x] != val:          # if the index value is not the same as the desired value, copy nums[x] into nums[i].  This will delete the wanted values from the list.
                nums[i] = nums[x]
                i += 1
        return i    # we don't return the list but we return the len of the list


