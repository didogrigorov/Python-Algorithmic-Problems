from typing import List


# def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
#      result = 0
#      current_sum = sum(arr[:k-1])
#
#      for L in range(len(arr) - k + 1):
#          current_sum += arr[L + k - 1]
#          if (current_sum / k) >= threshold:
#              result += 1
#          current_sum -= arr[L]
#
#      return result

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    result = 0
    right = k

    for l in range(len(arr)):
        current_sum = sum(arr[l:right])

        if current_sum / k >= threshold:
            result += 1
            if right < len(arr):
                right += 1
            else:
                break
        else:
            right += 1

    return result


arr = [1,1,1,1,1] #6
k = 1
threshold = 0
print(numOfSubarrays(arr, k, threshold))