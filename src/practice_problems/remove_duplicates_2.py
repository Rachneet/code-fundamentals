"""
Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying 
the input array in-place with O(1) extra memory.

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, 
the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    
    count = 1
    i = 1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1

            if count > 2:
                nums.pop(i)
                i -= 1
                count -= 1
        else:
            count = 1

        i+=1

    return i


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    res = removeDuplicates(nums)
    print(res)
