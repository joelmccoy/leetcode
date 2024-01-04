from reverse_polish_notation import Solution


def test_solution():
    sol = Solution()

    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        sol.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )
    assert sol.evalRPN(["4", "-2", "/", "2", "-3", "-", "-"]) == -7
