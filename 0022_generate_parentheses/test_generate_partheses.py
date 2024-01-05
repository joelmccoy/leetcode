from generate_parentheses import Solution


def test_solution():
    sol = Solution()
    assert sol.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    assert sol.generateParenthesis(1) == ["()"]
