from valid_parentheses import Solution


def test_valid():
    sol = Solution()

    assert sol.isValid("()")
    assert not sol.isValid("(")
    assert not sol.isValid("(]")
    assert not sol.isValid("]]")
    assert sol.isValid("[]([])[[[]]]")
