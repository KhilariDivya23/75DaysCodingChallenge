class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col, m = len(matrix)-1, 0, len(matrix[0])
        while row >= 0 and col < m:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
