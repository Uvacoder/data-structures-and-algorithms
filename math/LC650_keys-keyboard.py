class Solution:
    def minSteps(self, n: int) -> int:
        # prime factorization approach. (This can also be solved using dynamic programming.)
        
        # what is prime factorization? 
        # https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization
        
        ans = 0
        d = 2
        
        while n > 1:
            while n % d == 0:   # finds the facors of 'n'
                ans = ans + d
                n = n / d
            d = d + 1
            
        return ans
