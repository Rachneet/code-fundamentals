"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 
Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    
    n = len(nums)
    majority_condition = n/2

    seen = {}
    for i in range(n):
        if nums[i] not in seen.keys():
            seen[nums[i]] = 1
        else:
            seen[nums[i]] += 1

    maj_element = [k for k,v in seen.items() if v > majority_condition][0]

    return maj_element


if __name__ == "__main__":
    nums = [3, 2, 3]
    res = majorityElement(nums)
    print(res)