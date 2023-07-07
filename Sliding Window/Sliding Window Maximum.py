import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    result = []
    myqueue = collections.deque()
    l = r = 0

    while r < len(nums):
        while myqueue and nums[myqueue[-1]] < nums[r]:
            myqueue.pop()
        myqueue.append(r)

        if l > myqueue[0]:
            myqueue.popleft()

        if (r + 1) >= k:
            result.append(nums[myqueue[0]])
            l += 1

        r += 1

    return result


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))