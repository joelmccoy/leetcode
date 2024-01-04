# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = "+-*/"

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                val2, val1 = stack.pop(), stack.pop()
                result = 0
                match token:
                    case "*":
                        result = val1 * val2
                    case "/":
                        result = int(val1 / val2)
                    case "+":
                        result = val1 + val2
                    case "-":
                        result = val1 - val2

                stack.append(result)

        return stack[-1]
