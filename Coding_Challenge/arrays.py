from typing import List
from collections import Counter

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

        min_price = prices[0]
        max_price = prices[0]
        min_index = 0
        max_index = 0
        profit = 0

        for index, price in enumerate(prices):
            if price < max_price:
                min_price = price
                min_index = index

            if price >= min_price:
                max_price = price
                max_index = index

            if max_index > min_index:
                delta = max_price - min_price
                profit += delta

                # reset pointers
                min_price = price
                max_price = price
                min_index = index
                max_index = index

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
            return

        nums.sort()

        if len(nums) == 1:
            return False

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True
        return False

    @staticmethod
    def contains_duplicate_fast_set(self, nums: List[int]) -> bool:
        """ Very fast solution (not mine) and I want to keep it for educational purpose"""
        visited = set()
        for i in nums:
            if i in visited:
                return True
            visited.add(i)

    @staticmethod
    def contains_duplicate_full_slow_set(self, nums: List[int]) -> bool:
        """Another solution from leetcode, as a previous is made using set but os very slow.
        The difference is that set is created from from the whole List:
        Converting a list to a set requires that every item in the list be visited once, O(n).
        Inserting an element into a set is O(1), so the overall time complexity would be O(n)."""
        return len(nums) != len(set(nums))

#################################################################
    @staticmethod
    def single_number(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers nums,
        every element appears twice except for one.
        Find that single one.

        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0]

        visited = set()

        for i in nums:
            if i not in visited:
                visited.add(i)
            else:
                visited.remove(i)

        return visited.pop()

#################################################################
    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        """
            Given two integer arrays nums1 and nums2, return an array of their intersection.
            Each element in the result must appear as many times as it shows in both arrays
            and you may return the result in any order.

        """
        if not nums1 or not nums2:
            return False
        if len(nums1) == 1 and len(nums2) == 1:
            if nums1[0] == nums2[0]:
                return nums1

        intersection = list()

        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                intersection.append(x)
        return intersection

    @staticmethod
    def intersect_counter(nums1: List[int], nums2: List[int]) -> List[int]:
        """ Very fast solution (not mine) and I want to keep it for educational purpose"""
        c = dict(Counter(nums1))

        res = []
        for e in nums2:
            if e in c and c[e] > 0:
                c[e] -= 1
                res.append(e)

        return res

    #################################################################
    @staticmethod
    def plus_one_best(digits: List[int]) -> List[int]:
        """ Better solution with carry-out - 52 ms
         Given a non-empty array of decimal digits representing a non-negative integer,
         increment one to the integer.

         The digits are stored such that the most significant digit is at the head of the list,
         and each element in the array contains a single digit.

         You may assume the integer does not contain any leading zero, except the number 0 itself.
         """
        if not digits:
            return

        num = 0
        power = 1

        # obtain represented positive number from a list
        for i in range(len(digits) - 1, -1, -1):
            num += (digits[i] % 10) * power
            power *= 10

        # increment
        num += 1

        # convert back into list
        digit_string = str(num)
        # Convert each character of `digit_string` to an integer.
        digit_map = map(int, digit_string)
        # Convert `digit_map` to a list.
        digit_list = list(digit_map)

        return digit_list

    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        """ Not so ideal as previous but faster: 32 ms
         Given a non-empty array of decimal digits representing a non-negative integer,
         increment one to the integer.

         The digits are stored such that the most significant digit is at the head of the list,
         and each element in the array contains a single digit.

         You may assume the integer does not contain any leading zero, except the number 0 itself.
         """
        if not digits:
            return

        num = 0
        power = 1

        # obtain represented positive number from a list
        for i in range(len(digits) - 1, -1, -1):
            num += (digits[i] % 10) * power
            power *= 10

        # increment
        num += 1

        # convert back into list
        digit_string = str(num)
        # Convert each character of `digit_string` to an integer.
        digit_map = map(int, digit_string)
        # Convert `digit_map` to a list.
        digit_list = list(digit_map)

        return digit_list

    #################################################################

    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        """
        Move all the 0's to the end of array.
        All the non-zero elements must retain their original order.

        Both the requirements are mutually exclusive,
        i.e., you can solve the individual sub-problems and then
        combine them for the final solution.
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                left += 1

    #################################################################

    @staticmethod
    def find_missing(nums):
        """
         You are given an array of positive numbers from 1 to n,
         such that all numbers from 1 to n are present except one number x.
         You have to find x. The input array is not sorted.

         Find the sum sum_of_elements of all the numbers in the array.
         This would require a linear scan, O(n).

         Then find the sum expected_sum of first n numbers
         using the arithmetic series sum formula

         The difference between these i.e. expected_sum - sum_of_elements,
         is the missing number in the array.
        """
        # calculate sum of all elements
        # in input list
        sum_of_elements = sum(nums)

        # There is exactly 1 number missing
        n = len(nums) + 1
        actual_sum = (n * (n + 1)) / 2
        return actual_sum - sum_of_elements

    #################################################################

    @staticmethod
    def find_sum_of_two(A, val):
        """
         Given an array of integers and a value, determine if there are any two integers
         in the array whose sum is equal to the given value. Return true if the sum exists
         and return false if it does not.

         Scan the whole array once and store visited elements in a hash set.

         During scan, for every element e in the array, we check if val - e is present in the hash set
         i.e. val - e is already visited.

         If val - e is found in the hash set, it means there is a pair (e, val - e) in array
         whose sum is equal to the given val.

         If we have exhausted all elements in the array and didn’t find any such pair,
         the function will return false
         """
        found_values = set()
        for a in A:
            if val - a in found_values:
                return True

            found_values.add(a)

        return False

    #################################################################

    @staticmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
         Same task but in a given  array of integers nums and an integer target,
         return indices of the two numbers such that they add up to target.

         """
        found = {}

        for idx, value in enumerate(nums):
            rest = target - nums[idx]
            if rest in found:
                return [idx, found[rest]]
            else:
                found[value] = idx

    #################################################################

    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        """
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        """

        if not board:
            return False
        if len(board) != 9:
            return False

        # Validate Rule1: the Row

        for i in board:
            stack = []
            for e in i:
                if (e != ".") and (e in stack):
                    return False
                stack.append(e)

        # Validate Rule 2: the Column
        for j in range(9):
            stack = []
            for i in range(9):
                if (board[i][j] != ".") and (board[i][j] in stack):
                    return False
                stack.append(board[i][j])

        # Valiedate Rule 3: the subbox
        for r in range(3):

            for c in range(3):
                stack = [
                    *board[3 * r][3 * c:3 * c + 3],
                    *board[3 * r + 1][3 * c:3 * c + 3],
                    *board[3 * r + 2][3 * c:3 * c + 3]
                ]
                saw = []
                for e in stack:
                    if (e != ".") and (e in saw):
                        return False
                    saw.append(e)

        return True

    #################################################################

    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        """
        You are given an n x n 2D matrix representing an image,
        rotate the image by 90 degrees (clockwise).
        """
        if matrix is None:
            return

        # transpose
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        # reflect
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0]) // 2):
                reflection = len(matrix[0]) - j - 1
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][reflection]
                matrix[i][reflection] = temp