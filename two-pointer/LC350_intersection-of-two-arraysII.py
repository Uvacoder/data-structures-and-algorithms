class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # two pointer appraoch:
        i = 0
        j = 0
        intersection = []
        
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:   # if both numbers == each other
                intersection.append(nums1[i])
                i += 1
                j += 1
                
        return intersection
