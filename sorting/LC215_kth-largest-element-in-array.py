class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using the Sorting method:
        nums.sort()
        return nums[-k]
