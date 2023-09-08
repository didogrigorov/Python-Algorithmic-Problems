class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        cars_stack = []

        for p, s in sorted(pair)[::-1]:
            cars_stack.append((target - p) / s)
            if len(cars_stack) >= 2 and cars_stack[-1] <= cars_stack[-2]:
                cars_stack.pop()

        return len(cars_stack)