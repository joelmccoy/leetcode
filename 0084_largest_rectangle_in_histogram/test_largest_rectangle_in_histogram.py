from largest_rectangle_in_histogram import Solution


def test_solution():
    sol = Solution()

    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
