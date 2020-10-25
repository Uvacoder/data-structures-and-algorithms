class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []  
        n1 = nums[:n]
        n2 = nums[n:]
        i = 0
        
        for x in range(len(n1)) and range(len(n2)):
          output.append(n1[x])
          output.append(n2[x])
          
        return output
