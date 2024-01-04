from min_stack import MinStack


def test_minstack():
    results = []
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    results.append(minStack.getMin())
    minStack.pop()
    results.append(minStack.top())
    results.append(minStack.getMin())

    assert results == [-3, 0, -2]
