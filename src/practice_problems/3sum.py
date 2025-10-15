"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    """
    very naive approach
    """
    
    if len(nums) == 3 and sum(nums) == 0:
        return [[0] * len(nums)]
    elif len(nums) == 3 and sum(nums) != 0:
        return []
    
    triplets = set()
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+2, n):

                if nums[i]+nums[j]+nums[k] == 0:
                    triplets.add([nums[i], nums[j], nums[k]])

    return  triplets


def threeSum_v2(nums: List[int]) -> List[List[int]]:

    """
    correct approach
    """
    
    n = len(nums)
    res = set()
    dups = set()

    seen = dict()  # dict of complement and ids

    for i in range(n):
        if nums[i] not in dups:
            dups.add(nums[i])
        for j in range(i+1, n):
            complement = -nums[i] - nums[j]
            if complement in seen and seen[complement] == i:
                res.add(tuple(sorted((nums[i], nums[j], complement))))

            seen[nums[j]] = i

    return [list(x) for x in res]



    

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    # nums = [0, 1, 1]
    # nums = [0, 0, 0]
    res = threeSum_v2(nums)
    print(res)
