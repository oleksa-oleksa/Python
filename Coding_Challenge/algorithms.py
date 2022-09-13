from typing import List

def search(self, nums: List[int], target: int) -> int:
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
    
    while (right_idx != left_idx and mid_idx >= left_idx and mid_idx <= right_idx ):
        
        mid_idx = int((left_idx + right_idx) / 2)
        print(mid_idx)
        if nums[mid_idx] == target:
            return mid_idx;

        elif target < nums[mid_idx]:
            right_idx = right_idx - 1

        elif target > nums[mid_idx]:
            left_idx = left_idx +  1            
            
    return -1
    