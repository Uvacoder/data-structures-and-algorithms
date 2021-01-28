class Solution:
    def reverseWords(self, s: str) -> str:
        # Using join() function and split() function and python slice notation
        # Understanding slice notation: https://stackoverflow.com/questions/509211/understanding-slice-notation
        # [::-1] => all items in the list, reversed
        return " ".join(s.split()[::-1])
