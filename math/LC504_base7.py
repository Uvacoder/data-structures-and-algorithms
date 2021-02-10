class Solution:
    def convertToBase7(self, num: int) -> str:
        base7 = []
        
        if num == 0:
            return "0" 
        
        elif num < 0:
            #remove the negative sign
            num = str(num)
            num = int(num[1:])
            
            while num != 0:
                remainder = str(num % 7)
                num = int(num / 7)
                base7.insert(0, remainder)
            
            #adding the negative sign
            base7.insert(0, '-')
            base7 = "".join(base7)
            return base7
            
        else: 
            while num != 0:
                remainder = str(num % 7)
                num = int(num / 7)
                base7.insert(0, remainder)
            base7 = "".join(base7)
            return base7


