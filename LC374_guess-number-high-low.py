# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1
        while low <= high:
            middle = (high + low) // 2  # floor division
            
            if guess(middle) == 0:
                return middle
            if guess(middle) == -1: # number is lower
                high = middle -1
            else:                   # number is higher
                low = middle + 1
        
        return low 
