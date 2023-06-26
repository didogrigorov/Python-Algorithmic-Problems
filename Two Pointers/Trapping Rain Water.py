from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) -1
    left_max, right_max = height[left], height[right]
    result = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            result += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            result += right_max - height[right]

    return result


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))