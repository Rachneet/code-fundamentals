"""
Given an integer array nums and an integer val, remove all occurrences of 
val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the 
elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


from typing import List

def removeElement(nums: List[int], val: int) -> int:
    n = len(nums)

    reader = 0
    writer = 0

    while reader < n:
        if nums[reader] == val:
            reader += 1
        else:
            nums[writer] = nums[reader]
            reader += 1
            writer += 1

    return writer


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3

    removeElement(nums, val)
    