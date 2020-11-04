class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# Python Method
        return sorted(s) == sorted(t)



        # if len(s) != len(t):
        #   return False
        
# Hash Table Method
        # letterCount = {}  # Using dictionary
        # for x in s:
        #   if x not in letterCount:  # if the letter is not in the dictionary, add it and add 1 to the count
        #     letterCount[x] = 1
        #   else:  # if the letter is already in the dictionary, add the count
        #     letterCount[x] += 1
    
        # # Comparing s to t
        # for x in t:
        #   if x not in letterCount:  # if the letter is not in s
        #     return False
        #   if letterCount[x] < 1:    # if the letter count is below 0
        #     return False
        #   
        #   letterCount[x] -= 1
        #   
        # return True 
