class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)

        n = len(matrix[0])
        
        row,col = 0, n-1
        
        while row<=m-1 and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col -= 1
            else:
                row += 1
        return False
