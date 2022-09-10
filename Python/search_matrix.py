'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return target in row

# Tests
soln = Solution()
print(soln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(soln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False

# Runtime: 67ms
# Memory: 14.3 MB