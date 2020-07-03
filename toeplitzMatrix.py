class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a,i = 1,1
        if (len(matrix[a-1]) == 1):
            return True  
        while (a != len(matrix) ):
            if (matrix[a][i] != matrix[a-1][i-1]):
                return False
            if (i + 1 == len(matrix[0])):
                a += 1
                i = 1
            else:
                i += 1
        return True