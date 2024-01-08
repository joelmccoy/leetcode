# https://leetcode.com/problems/koko-eating-bananas/
from typing import List


class Solution:
    def get_time_to_eat_piles(self, piles, speed):
        time_to_eat = 0
        for pile in piles:
            time_to_eat_pile = -(pile // -speed)
            time_to_eat += time_to_eat_pile
        return time_to_eat

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_speed = r
        while l <= r:
            m = (r + l) // 2
            time_to_eat = self.get_time_to_eat_piles(piles, m)
            if time_to_eat <= h:
                r = m - 1
                min_speed = min(min_speed, m)
            elif time_to_eat > h:
                l = m + 1

        return min_speed
