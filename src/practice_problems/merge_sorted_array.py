from typing import List


def merge_naive(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

    naive approach
    """
    
    for i in range(n):
        nums1[m+i] = nums2[i]

    nums1.sort()



if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    res = merge_naive(
        nums1=nums1,
        m=m,
        nums2=nums2,
        n=n,
    )
    print(res)