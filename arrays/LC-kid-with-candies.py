class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      highest_candy_in_array = max(candies)
      output = []

      for x in range(len(candies)):
        numCandies = candies[x] + extraCandies
        
        if numCandies >= highest_candy_in_array:
          output.append(True) 
        else:
          output.append(False) 
          
      return output
    
#        1. find max integer in array
#        2. add extraCandies to each index of array 
#          3. see if that is >= max integer in array
