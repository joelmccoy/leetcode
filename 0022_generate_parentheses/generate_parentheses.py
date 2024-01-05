# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(num_open: int, num_close: int, current: str = ""):
            if num_close == num_open == n:
                results.append(current)
                return

            if num_open < n:
                backtrack(num_open + 1, num_close, current + "(")

            if num_close < n and num_open > num_close:
                backtrack(num_open, num_close + 1, current + ")")

            return

        backtrack(0, 0, "")
        return results
