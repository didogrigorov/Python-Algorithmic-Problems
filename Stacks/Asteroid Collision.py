from typing import List
def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff > 0:
                a = 0
            elif diff < 0:
                stack.pop()
            else:
                a = 0
                stack.pop()
        if a:
            stack.append(a)

    return stack
asteroids = [-1, 3, 2, -3]
print(asteroidCollision(asteroids))