class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer approach:
            # if sum is > target,  right pointer moves
            # if sum is < target, left pointer moves
            
        # adds 0 to beginning of the list
        numbers.insert(0,0)
        left = 1
        right = len(numbers) - 1
        
        while left <= right:
            sumOfNumbers = numbers[left] + numbers[right]
            
            if sumOfNumbers > target:
                right -= 1
            if sumOfNumbers < target:
                left += 1
            if sumOfNumbers == target:
                return [left, right]
