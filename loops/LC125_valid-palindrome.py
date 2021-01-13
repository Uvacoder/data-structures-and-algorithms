# you can find this same problem in my strings directory 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_string = ""
        for x in s:
            if x.isalnum():
                temp_string = temp_string + x.lower()
        
        left = 0
        right = len(temp_string) - 1
        
        while (left < right):
            if temp_string[left] != temp_string[right]:
                return False
            left += 1
            right -= 1
        return True
