class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Using python reverse method
            # return s.reverse()
        
        # Approach 2: Two pointers
        left = 0
        right = len(s) - 1
        
        while (left < right):
            temp = s[left]
            s[left] = s[right] 
            s[right] = temp
            
            # left = left + 1
            # right = right - 1 
            left += 1
            right -= 1
        
