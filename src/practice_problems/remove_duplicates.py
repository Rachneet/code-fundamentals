"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain 
the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    
    n = len(nums)
    seen = []

    reader, writer = 0, 0

    while reader < n:
        if nums[reader] in seen:
            reader += 1
        else:
            nums[writer] = nums[reader]
            seen.append(nums[reader])

            reader += 1
            writer += 1

    return writer


if __name__ == "__main__":
    nums = [1,1,2]
    res = removeDuplicates(nums=nums)
    print(res)
