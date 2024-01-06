from car_fleet import Solution


def test_solution():
    sol = Solution()

    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    assert sol.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1
