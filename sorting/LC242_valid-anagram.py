class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Approach 1: Sorting
        # # Using built-in sorting library
        # if sorted(s) != sorted(t):
        #     return False
        # else:
        #     return True
        
        
        # Approach 2: Hash Table
        counter = {} # Using dictionary
        for x in s:
            if x not in counter:
                counter[x] = 1 
            else:
                counter[x] += 1
                
        for x in t:
            if x not in counter:
                return False
            if counter[x] < 1:
                return False
            counter[x] -= 1
            
            
        # Test case of when s = "ab" and t = "a" 
        for x in s:
            if counter[x] > 0:
                return False
        
        return True
