class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Two pointer approach:
        # 1 pointer in nums1 and another pointer in nums2
        first = m - 1
        second = n - 1
        
        for x in range((m + n - 1), -1, -1):    # going in reverse order
            if second < 0:
                break
            
            if first >= 0 and nums1[first] > nums2[second]:      # if nums2 has a higher value
                nums1[x] = nums1[first]
                first -= 1
            else:       # if nums1 has a higher value
                nums1[x] = nums2[second]
                second -= 1
        
        # My Approach
        # # using python built-in functions
        # # first we replace the 0's and put in nums2's values inside nums1
        # # then we sort it 
        # nums2_tracker = 0
        # for x in range(m, len(nums1)):
        #     if nums1[x] == 0:
        #         nums1[x] = nums2[nums2_tracker]
        #         nums2_tracker += 1
        
