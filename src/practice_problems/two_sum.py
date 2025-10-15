
def two_sum_v1(arr: list, target: int) -> bool: 
    """
    Given an array arr[] of n integers and a target value, 
    check if there exists a pair whose sum equals the target.
    """

    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return True
            
    return False


def two_sum_v2(arr: list, target: int):
    """
    Given an array arr[] of n integers and a target value, 
    check if there exists a pair whose sum equals the target.
    """

    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        
        elif sum < target:
            left += 1
        
        else:
            right -= 1

    return False


def two_sum_v3(arr: list, target: int):
    """
    use hash set for most efficiency
    """

    seen = set()

    for num in arr:

        complement = target - num

        if complement in seen:
            return True

        seen.add(num)
    
    return False
        


if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -4

    res = two_sum_v2(arr, target)
    print(res)