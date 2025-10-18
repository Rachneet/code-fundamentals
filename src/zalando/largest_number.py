"""
Given a list of non-negative integers nums, arrange them such that 
they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

"""

from typing import List


def largestNumber(nums: List[int]) -> str:
    
    nums = [str(n) for n in nums]
    nums.sort(key=lambda a: a*10, reverse=True)
    
    if nums[0] == "0":
        return "0"
    
    return "".join(nums)


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    res = largestNumber(nums=nums)
    print(res)
