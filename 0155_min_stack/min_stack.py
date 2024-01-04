# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        # tuple (val, min_val)
        self.stack: list[tuple(int, int)] = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            top = self.stack[-1]
            new_min = min(top[1], val)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
