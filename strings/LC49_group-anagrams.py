# This was my way but edge cases made it fail
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Catagorizing by Sorted String
#         anagramDictionary = {} 
#         
#         for x in strs:
#           ordered = sorted(x)
# # NOTE:
# # You don't have to use an if statement, dictionaries automatically puts the values according to the keys
#           if tuple(ordered) not in anagramDictionary: 
#             anagramDictionary[tuple(ordered)] = x.split()  # Uses split() to turn the values into a list
#           else:
#             # If the anagram is already in the dictionary, add the string as a value with the matching key 
#             anagramDictionary[tuple(ordered)].append(x)
#             
#         return anagramDictionary.values()

# The official way
# Categorizing by Sorted String
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagramDictionary = collections.defaultdict(list)  
      # if your accessing a value in the dictionary and it's not there, it defaults into a list
      # source: https://www.geeksforgeeks.org/defaultdict-in-python/

      for x in strs:
        ordered = sorted(x) # sorts the string into a list of characters => we want it into a tuple
        anagramDictionary[tuple(ordered)].append(x)

      return anagramDictionary.values()
