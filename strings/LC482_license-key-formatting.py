class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        alphaNum = "".join(S.split('-')).upper()
        dash = '-'
        remainder = len(alphaNum) % K
        
        # I suck at python slice notation 
        if remainder != 0:
            combined = alphaNum[:remainder]   # prints the first characters minus 1
            for x in range(remainder, len(alphaNum), K):
                print(x)
                combined = combined + '-' + alphaNum[x:x+K]
            return combined
            
        else:
            combined = alphaNum[:K]
            for x in range(K, len(alphaNum), K):
                combined = combined + '-' + alphaNum[x:x+K]
            return combined
