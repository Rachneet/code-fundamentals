"""
Given an array arr[] of n integers, construct a product array res[] (of the same size) 
such that res[i] is equal to the product of all the elements of arr[] except arr[i]. 
"""

def product_except_self(arr: list):

    """
    Naive approach with two loops
    """

    n = len(arr)
    res = [1] * n

    for i in range(n):
        for j in range(n):
            if i != j:
                res[i] *= arr[j]

    return res


def product_except_self_v2(arr: list):
    """
    The idea is to handle two special cases of the input array: when it 
    contains zero(s) and when it doesn't.

    If the array has no zeros, product of array at any index (excluding itself) 
    can be calculated by dividing the total product of all elements by the current element. 

    However, division by zero is undefined, so if there are zeros in the array, the logic changes. 

    If there is exactly one zero, the product for that index will be the product of all other 
    non-zero elements, while the elements in rest of the indices will be zero. 

    If there are more than one zero, the product for all indices will be zero, 
    since multiplying by zero results in zero.
    """

    n = len(arr)

    prod = 1
    zeros = 0
    idx = -1

    res = [0] * n

    for i in range(n):
        if arr[i] == 0:
            zeros += 1
            idx = i
        else:
            prod *= arr[i]

    if zeros == 0:
        for i in range(n):
            res[i] = prod / arr[i]
    elif zeros == 1:
        res[idx] = prod

    return res



if __name__ == "__main__":
    arr = [10, 0, 5, 6, 0]
    res = product_except_self_v2(arr)
    print(res)
