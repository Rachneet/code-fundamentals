"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array 
[1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.
"""

from typing import List

def maxArea(height: List[int]) -> int:
    
    n = len(height)
    left = 0
    right = n - 1

    area = 0

    while left < right:

        if height[left] <= height[right]:
            area = max(area, (right-left) * height[left])
            left += 1
        else:
            area = max(area, (right-left) * height[right])
            right -= 1

    return area
            

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    area = maxArea(height=height)
    print(area)