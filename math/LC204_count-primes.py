class Solution:
    def countPrimes(self, n: int) -> int:
        # A number is called prime if it's bigger than 1, and doesn't have any divisors other than 1 and itself.
        # output = NUMBER of prime numbers 
        # How many prime numbers are there that are less than n?
        if n <= 2:
            return 0
        
        # Sieve of eratosthenes algorithm:
        # source: https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
        
        # create an array of 'n' numbers of True
            # True meaning that, that index is a prime number
        # start with the assumption that everything is a prime number
        nums = [True] * n
        numOfPrime = 0
        
        # flip its multiples to false
        sqrt = int(n**0.5) + 1
        for x in range(2, sqrt):    # this traverses through the list
            if nums[x] == True:
                for y in range(x*x, n, x):   #this finds the multiples
                    nums[y] = False
            
        for x in range(2, n): 
            if nums[x] == True:
                numOfPrime += 1
        
        return numOfPrime
