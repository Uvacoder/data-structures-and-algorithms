class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastValue = output[-1][1]
            
            if start <= lastValue:
                output[-1][1] = max(lastValue, end)
            else:
                output.append([start,end])
                
        return output
