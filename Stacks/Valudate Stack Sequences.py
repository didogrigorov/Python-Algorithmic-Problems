from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    i = 0
    stack = []
    for n in pushed:
        stack.append(n)
        while i < len(popped) and stack and popped[i] == stack[-1]:
            stack.pop()
            i += 1

    return not stack

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))