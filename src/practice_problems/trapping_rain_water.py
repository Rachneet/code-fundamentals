"""
Given an array arr[] of size n consisting of non-negative integers, 
where each element represents the height of a bar in an elevation map 
and the width of each bar is 1, determine the total amount of water 
that can be trapped between the bars after it rains.

Input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides
"""

def trap_water(arr: list):

    """
    naive approach
    """

    n = len(arr)
    res = 0

    for i in range(n):

        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])


        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        res += min(left, right) - arr[i]

    return res


def trap_water_v2(arr: list):
    """
    two pointer approach
    """

    left  = 1
    right = len(arr) -2

    lmax = arr[left-1]
    rmax = arr[right+1]

    res = 0
    while left <= right:

        if rmax <= lmax:
            res += max(0, rmax - arr[right])
            rmax = max(rmax, arr[right])
            right -= 1
        else:
            res += max(0, lmax - arr[left])
            lmax = max(lmax, arr[left])
            left += 1

    return res



if __name__ == "__main__":
    arr = [3, 0, 2, 0, 4]
    res = trap_water_v2(arr)
    print(res)