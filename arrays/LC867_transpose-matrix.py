class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        for x in range(len(matrix[0])):   # traverses by single index
            temp = []
            
            for y in range(len(matrix)):  # this is how many lists inside the list, => traverses list by list
                temp.append(matrix[y][x])
            output.append(temp)

        return output
