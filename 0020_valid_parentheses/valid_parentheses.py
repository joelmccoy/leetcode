# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "[({":
                stack.append(char)

            if char in "])}":
                expected_on_stack = ""
                match char:
                    case "]":
                        expected_on_stack = "["
                    case "}":
                        expected_on_stack = "{"
                    case ")":
                        expected_on_stack = "("

                if len(stack) == 0:
                    return False

                if stack.pop() != expected_on_stack:
                    return False

        if len(stack) == 0:
            return True

        return False
