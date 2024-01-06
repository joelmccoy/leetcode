# https://leetcode.com/problems/car-fleet/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_combined = sorted(zip(position, speed), key=lambda x: x[0])
        number_of_fleets = 1
        stack = []  # time to arrive

        times_to_arrive = []
        for x in sorted_combined:
            times_to_arrive.append((target - x[0]) / x[1])

        for idx in range(len(times_to_arrive) - 1, -1, -1):
            if not stack:
                stack.append(times_to_arrive[idx])
                continue

            if times_to_arrive[idx] > stack[-1]:
                number_of_fleets += 1
                stack.append(times_to_arrive[idx])

        return number_of_fleets
