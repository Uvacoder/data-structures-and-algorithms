# you can find the same problem in my 'strings' directory

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charSplit = []
        charDict = {}
        for x in strs:
            charSplit.append(list(x))
        for x in range(len(charSplit)):
            charSplit[x].sort()
            charSplit[x] = tuple(charSplit[x])  # we turn into tuple because we want charSplit to be the key inside charDict.  Keys cannot be a 'list' because they cannot be hashed thus we turn it into a tuple
            
            if charSplit[x] not in charDict.keys():
                #put into dictionary
                charDict[charSplit[x]] = [strs[x]]
            else:
                # add into the values
                charDict[charSplit[x]].append(strs[x])
        return charDict.values()
        
