"""
Given an array arr[] of non-negative integers, where each element arr[i] represents the height 
of the vertical lines, find the maximum amount of water that can be contained between any two 
lines, together with the x-axis.

Examples :  

Input: arr[] = [1, 5, 4, 3]
Output: 6
Explanation: 5 and 3 are 2 distance apart. So the size of the base = 2. 
Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6.

Input: arr[] = [3, 1, 2, 4, 5]
Output: 12
Explanation: 5 and 3 are 4 distance apart. So the size of the base = 4. 
Height of container = min(5, 3) = 3. So total area = 4 * 3 = 12.

Input: arr[] = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25
Explanation: 8 and 5 are 5 distance apart. So the size of the base = 5. 
Height of container = min(8, 5) = 5. So, total area = 5 * 5 = 25.
"""

def container_with_water(arr: list):
    
    n = len(arr)
    res = 0

    for i in range(n):
        for j in range(i+1, n):
            base = j - i
            height = min(arr[i], arr[j])
            area = base * height

            res = max(res, area)

    return res


def container_with_water_v2(arr: list):
    """
    two-pointer solution
    """
    n = len(arr)
    left = 0
    right = n - 1
    result = 0

    while left < right:
        area = (right-left) * min(arr[left], arr[right])
        result = max(result, area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return result


if __name__ == "__main__":
    arr =  [2, 1, 8, 6, 4, 6, 5, 5]
    res = container_with_water_v2(arr)
    print(res)