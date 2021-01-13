class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numToString = str(n)
        product = 1
        sum = 0
        
        for x in numToString:
            sum = sum + int(x)
        for x in numToString:
            product = product * int(x)
        
        return product - sum
