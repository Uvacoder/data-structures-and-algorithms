class Solution:
    def myPow(self, x: float, n: int) -> float:
        # binary exponentiation approach
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n      # turn it into positive number
            
        answer = 1
        while n > 0:
            if n % 2 == 0:      # if n = even number
                x = x * x
                n = n / 2
                # print(x, n)
                
            else:
                answer = answer * x
                n -= 1
                # print("else: ", x, n)
        return answer
