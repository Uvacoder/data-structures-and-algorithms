class Solution:
    def reverseVowels(self, s: str) -> str:
        # not solved using the two pointer approach
        # solved using stacks
        vowel_stack = []
        word = ""
        vowels = 'aeiouAEIOU'
        
        for x in s:
            if x in vowels:
                vowel_stack.append(x)
        
        
        for x in s:
            if x not in vowels:
                word = word + x
            else:
                word = word + vowel_stack.pop()

        return word
