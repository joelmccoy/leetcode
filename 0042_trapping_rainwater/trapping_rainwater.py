# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # get max left values
        max_left = []
        for idx in range(len(height)):
            if idx == 0:
                prev = 0
            else:
                prev = max_left[idx - 1]
            max_left.append(max(height[idx], prev))

        max_right = [0] * len(height)
        for idx in range(len(height) - 1, -1, -1):
            if idx == len(height) - 1:
                prev = 0
            else:
                prev = max_right[idx + 1]

            max_right[idx] = max(height[idx], prev)

        trapped = 0
        for idx, val in enumerate(height):
            can_hold = min(max_left[idx], max_right[idx]) - val
            if can_hold > 0:
                trapped += can_hold

        return trapped
