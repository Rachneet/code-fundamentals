"""
Given an integer array nums, rotate the array to the right by k steps, 
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Naive approach
    """

    n = len(nums)
    # speed up rotation
    k %= n

    for i in range(k):
        previous = nums[-1]
        for j in range(n):
            nums[j], previous = previous, nums[j]


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Better approach
    """

    n = len(nums)
    k %= n

    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] = nums[i]

    for i in range(n):
        nums[i] = rotated[i]


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3

    res = rotate(nums=nums, k=k)
    print(res)
