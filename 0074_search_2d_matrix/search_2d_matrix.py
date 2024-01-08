# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search rows
        l, r = 0, len(matrix) - 1

        row_idx = 0

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                row_idx = m
                break

        # binary search the row
        row = matrix[row_idx]

        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True

        return False
