# you can find this same problem in my 'loops' directory

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Sanitize the input string by removing spaces and lowercasing it
        s = s.lower()
        s = s.replace(" ", "")
        
        # Removing non-alphanumeric characters
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        
        # If empty return true
        if s == "":
            return True
        
        # Create a left and right pointer, initially at start and end of input string
        left = 0
        right = len(s) - 1
        
        
        while left < right:
                    
            # if character at left and right pointer are not the same, return False
            if s[left] != s[right]:
                return False
            
            left = left + 1
            right = right - 1
            
        # Return true if the entire string is a palindrome
        return True
            
