class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if (len(matrix) == 0 or not matrix or not matrix[0]):
            return []
        a,i,j = [],0,0
        row,col = len(matrix),len(matrix[0])
        while(i<row and j<col):
            a.append(matrix[i][j])
            count = i+j
            if(count % 2 == 0):
                if(j==col-1):
                    i += 1
                elif (i == 0):
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if(i == row-1):
                    j += 1
                elif(j == 0):
                    i += 1
                else:
                    j -= 1
                    i += 1
        return a