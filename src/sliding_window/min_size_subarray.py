"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or 
equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    
    result = float('inf')
    left = 0

    curr_sum = 0

    for right in range(len(nums)):
        
        curr_sum += nums[right]

        while curr_sum >= target:
           result = min(result, right - left + 1)
           curr_sum -= nums[left]
           left += 1

    return result if result != float('inf') else 0 
            


if __name__ == "__main__":
    target = 11
    nums = [1,2,3,4,5]

    res = minSubArrayLen(
        target=target,
        nums=nums
    )
    print(res)
