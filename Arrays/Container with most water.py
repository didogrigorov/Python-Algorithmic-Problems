from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    result = 0
    h = max(height)

    while left < right:
        result = max(result, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        elif height[right] <= height[left]:
            right -= 1

        if (right - left) * h <= result:
            break
    return result

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))