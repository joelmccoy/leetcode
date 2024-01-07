# https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            if not stack:
                stack.append((idx, height))
            else:
                if height < stack[-1][1]:
                    while stack and height < stack[-1][1]:
                        previous = stack.pop()
                        area = (idx - previous[0]) * previous[1]
                        max_area = max(area, max_area)
                    stack.append((previous[0], height))
                else:
                    stack.append((idx, height))

        for idx, height in stack:
            area = height * (len(heights) - idx)
            max_area = max(area, max_area)

        return max_area
