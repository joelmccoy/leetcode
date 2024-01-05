# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack: list[tuple[int, int]] = []  # [temp, idx]

        for idx in range(len(temperatures)):
            temperature = temperatures[idx]
            if idx == 0:
                stack.append((temperature, idx))
            else:
                while stack and temperature > stack[-1][0]:
                    popped = stack.pop()
                    popped_idx = popped[1]
                    result[popped_idx] = idx - popped_idx
                stack.append((temperature, idx))

        return result
