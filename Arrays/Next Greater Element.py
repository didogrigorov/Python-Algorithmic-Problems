from typing import List
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1Idx = { n : i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        current = nums2[i]

        while stack and current > stack[-1]:
            value = stack.pop()
            idx = nums1Idx[value]
            res[idx] = current

        if current in nums1Idx:
            stack.append(current)

    return res