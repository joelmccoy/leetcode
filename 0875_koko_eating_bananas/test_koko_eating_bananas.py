from koko_eating_bananas import Solution


def test_solution():
    sol = Solution()

    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
