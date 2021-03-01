class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # approach #1: sorting via custom comparator
        
        # convert each integer to a string.  Then, we sort the array of strings.
        # the sorted() function will create a new list containing a sorted version of the list it is given
        mapped = sorted(map(str, nums), key=LargerNumKey)   # key = a function to execute to decide the order
        
        
        # then we combine the string to make a big number
        # output = ''.join(mapped, key=LargerNumKey)
        largest_num = ''.join(mapped)
        if largest_num[0] == '0':
            return '0'
        return largest_num
