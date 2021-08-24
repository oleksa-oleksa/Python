from typing import List
"""
This is LeetCode's official curated list of Top classic interview question

"""


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        """
            Remove Duplicates from Sorted Array

            Given an integer array nums sorted in non-decreasing order,
            remove the duplicates in-place such
            that each unique element appears only once.
            The relative order of the elements should be kept the same.

            Template
            Use two pointers as slow runner and fast runner.
            Each of them flags a key point during traversal. In general, fast runner grows
            each iteration and slow runner grows with some restrictions.
            By that, we can process logic based on these two runners.


            # slow & fast runner: slow-> fast->->
            def slow_fast_runner(self, seq):
                # initialize slow runner
                slow = seq[0]   # for index: slow = 0
                # fast-runner grows each iteration generally
                for fast in range(seq):     # for index: range(len(seq))
                    #slow-runner grows with some restrictions
                    if self.slow_condition(slow):
                        slow = slow.next    # for index: slow += 1
                    # process logic before or after pointers movement
                    self.process_logic(slow, fast)

            We can use the fast runner to represent the current element
            and use the slow runner to flag the end of the new, non-duplicate array.

            """

        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            # compare element with a next one in order to find a duplicate in a non-decreasing array
            # if current element is unique,
            # slow runner grows one step and copys the current value
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

#################################################################

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        """
        You are given an array prices where prices[i]
        is the price of a given stock on the i_th day.

        Find the maximum profit you can achieve.
        You may complete as many transactions as you like
        (i.e., buy one and sell one share of the stock multiple times).
        """
        if not prices:
            return 0

        min_price = 0
        max_price = 0
        slow = 0
        profit = 0

        for fast in range(1, len(prices)):
            delta = prices[fast] - prices[slow]
            if delta > profit:
                profit = delta
            slow += 1
        return profit

#################################################################

    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        Given an array, rotate the array to the right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if k == 0:
            return nums

        while k > len(nums):
            k = k - len(nums)

        head = nums[-k:]
        tail = nums[:-k]

        nums[:-k] = head
        nums[-k:] = tail

    @staticmethod
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true
        if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        if not nums:
            return False
        nums.sort()
        if len(nums) == 1:
            return False

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    @staticmethod
    def contains_duplicate_v2(self, nums: List[int]) -> bool:
        """ It's not mine but very fast solution and I want to keep it for educational purpose"""
        visited = set()
        for i in nums:
            if i in visited:
                return True
            visited.add(i)
