"""
problem_name = Search a 2D Matrix
problem_source = https://leetcode.com/problems/search-a-2d-matrix/

Algo 
    - First we are gonna choose the right row where the target might exist, by conducting the binary search on the last element of each row
    - The we are gonna operate the binary search on that row
"""

from typing import Optional, List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Choosing the right row, read algo step 1
        row_hi = (
            len(matrix[0]) - 1
        )  # There will be atleast a row in the matrix a/q to constraints
        lo = 0
        hi = len(matrix) - 1

        if (
            target < matrix[lo][lo] or target > matrix[hi][row_hi]
        ):  # When target not in range
            return False

        while lo < hi:
            mid = (lo + hi) // 2

            if target > matrix[mid][row_hi]:
                lo = mid + 1
            elif target < matrix[mid][row_hi]:
                hi = mid
            else:
                return True

        # Now we've sorted the right row

        lo = 0

        while lo <= row_hi:
            mid = (lo + row_hi) // 2
            if (
                target < matrix[hi][mid]
            ):  # Here, 'hi' represents the right row of the matrix that might contain target
                row_hi = mid - 1
            elif target > matrix[hi][mid]:
                lo = mid + 1
            else:
                return True
        return False


solve = Solution()
result = solve.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
result = solve.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)
result = solve.searchMatrix([[1], [3]], 1)














#Another Approach

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, (m*n) - 1

        while l <= r:
            mid = (l + r) // 2
            i, j = divmod(mid, m)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
    
        return False