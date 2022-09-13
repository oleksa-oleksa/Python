from typing import List

def search(nums: List[int], target: int) -> int:
    """
    704. Binary Search

    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.
    """
    if nums is None:
        return -1
    if len(nums) == 1:
        if target == nums[0]:
            return 0
        else:
            return -1
    
    left_idx = 0
    right_idx = len(nums)
    mid_idx = int((left_idx + right_idx) / 2)
    
    while (right_idx != left_idx and mid_idx >= left_idx and mid_idx <= right_idx):
        
        mid_idx = int((left_idx + right_idx) / 2)
        print(mid_idx)
        if nums[mid_idx] == target:
            return mid_idx;

        elif target < nums[mid_idx]:
            right_idx = right_idx - 1

        elif target > nums[mid_idx]:
            left_idx = left_idx +  1            
            
    return -1
    
def firstBadVersion(n: int) -> int:
    """
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
    which causes all the following ones to be bad.
    You are given an API bool isBadVersion(version) which returns whether version is bad. 
    Implement a function to find the first bad version. You should minimize the number of calls to the API.
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

    # The isBadVersion API is already defined for you.
    # def isBadVersion(version: int) -> bool:
    """
    if n== 1:
        return (1 if isBadVersion(n) else -1)
        
    low = 1
    high = n
    while(low <= high):
        mid = (low+high)//2
        
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif isBadVersion(mid) and isBadVersion(mid-1):
            high = mid-1
        elif not isBadVersion(mid):
            low = mid+1
    return -1
 