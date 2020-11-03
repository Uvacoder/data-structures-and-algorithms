class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around center method
        if len(s) <= 1:
           return s
          
        start = 0
        end = 0 
        
        for i in range(len(s)):
          len1 = self.expandAroundCenter(s, i, i)
          len2 = self.expandAroundCenter(s, i, i + 1) # this is for when the string is an even number, it can center itself properly
          length = max(len1, len2)
          
          if(length > end - start):  # updates the longest palindromic substring
            start = i - (length - 1) // 2    # Use the integer division operator (//) to divide two numbers and round their quotient down to nearest integer.
            end = i + length // 2
            
        return s[start : end+1]
          
    # This function helps traverse the string      
    def expandAroundCenter(self, s: 'list', left: 'int', right: 'int') -> 'int':
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

      return right - left - 1
