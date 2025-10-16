"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List

def canJump(nums: List[int]) -> bool:
    n = len(nums)
    
    # memo[i] = 1 means "position i CAN reach the end"
    # memo[i] = -1 means "we don't know yet"
    memo = [-1] * n
    memo[-1] = 1  # Last position can always "reach" the end (it IS the end!)

    # Work backwards from second-to-last position
    for i in range(n-2, -1, -1):
        # Calculate the furthest we can jump from position i
        furthest_jump = min(i + nums[i], n-1)
        
        # Check all positions we can reach from i
        for j in range(i+1, furthest_jump+1):
            if memo[j] == 1:  # If any reachable position can reach the end
                memo[i] = 1   # Then position i can reach the end too!
                break         # No need to check further

    return memo[0] == 1  # Can we reach the end from position 0?



if __name__ == "__main__":
    nums = [2,3,1,1,4]
    res = canJump(nums=nums)
    print(res)