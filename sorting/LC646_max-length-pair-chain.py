class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Approach 2: Greedy
        # how we can add to our chain is by choosing the next addition to be the one with the lowest 2nd coordinate. 
        
        current = float('-inf')     # negative infinite value
        answer = 0
        
        for x,y in sorted(pairs, key = operator.itemgetter(1)):     # this for loop is sorting 'pairs' using index value 1.  'key' is how you want to sort it.  'operator.itemgetter' is getting the index value 1
        # this is increasing order in terms of their 2nd coordinate
            if current < x: 
                current = y
                answer += 1
                
        return answer
