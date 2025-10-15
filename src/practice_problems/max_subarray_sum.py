
def max_subarray_sum(arr: list):
    """
    Given an integer array arr[], find the subarray (containing at least one element) 
    which has the maximum possible sum, and return that sum.
    """

    res = arr[0]
    n = len(arr)

    for i in range(n):
        curr_sum = 0

        for j in range(i, n):
            curr_sum += arr[j]

            res = max(res, curr_sum)

    return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]  # 11
    print(max_subarray_sum(arr))