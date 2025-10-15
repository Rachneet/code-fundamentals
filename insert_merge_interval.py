"""
Given a set of non-overlapping intervals[][] where intervals[i] = [starti , endi] 
represent the start and the end of the ith event and intervals is sorted in 
ascending order by starti and a new interval, insert the interval at the correct 
position such that after insertion, the intervals remain sorted. 
If the insertion results in overlapping intervals, then merge the overlapping intervals. 
Assume that the set of non-overlapping intervals is sorted based on start time.

Examples: 

Input: intervals[][] = [[1, 3], [4, 5], [6, 7], [8, 10]], newInterval[] = [5, 6] 
Output: [[1, 3], [4, 7], [8, 10]]
Explanation: The intervals [4, 5] and [6, 7] are overlapping with [5, 6]. 
So, they are merged into one interval [4, 7]. 

Input: intervals[][] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval[]  = [4, 9]
Output: [[1, 2], [3, 10], [12, 16]]
Explanation: The intervals [ [3, 5], [6, 7], [8, 10] ] are overlapping with [4, 9]. 
So, they are merged into one interval [3, 10].
"""


def insert_merge_interval(intervals: list[list], new_interval: list):

    """
    naive approach
    """

    intervals.append(new_interval)
    intervals.sort()

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        if curr[0] <= last[1]:
            last[1] = max(curr[1], last[1])
        else:
            res.append(curr)

    return res


def insert_merge_interval(intervals: list[list], new_interval: list):

    """
    expected approach
    """

    pass
    


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 9] 
    res = insert_merge_interval(
        intervals=intervals,
        new_interval=new_interval
    )
    print(res)
