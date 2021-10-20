"""
This is LeetCode's official curated list of Top classic interview question

"""
import copy
from typing import List


class Solution:
    @staticmethod
    def can_segment_string(s, dictionary):

        """
        String segmentation
        You are given a dictionary of words and a large input string.
        You have to find out whether the input string can be completely segmented
        into the words of a given dictionary.

        Runtime Complexity: Exponential, O(2^n)
​​        Memory Complexity: Polynomial, O(n^2)

        """

        for i in range(1, len(s) + 1):
            first = s[0:i]
            if first in dictionary:
                second = s[i:]
                if not second or second in dictionary or can_segment_string(second, dictionary):
                    return True
        return False

    #################################################################

    @staticmethod
    def print_all_braces_rec(n, left_count, right_count, output, result):
        """
          Print all braces combinations for a given value n so that they are balanced.
          For this solution, we will be using recursion.
          """

        if left_count >= n and right_count >= n:
            result.append(copy.copy(output))

            if left_count < n:
                output += '{'
                print_all_braces_rec(n, left_count + 1, right_count, output, result)
                output.pop()

            if right_count < left_count:
                output += '}'
                print_all_braces_rec(n, left_count, right_count + 1, output, result)
                output.pop()

    def print_all_braces(n):
            output = []
            result = []
            print_all_braces_rec(n, 0, 0, output, result)
            return result

    #################################################################

    @staticmethod
    def reverseString(s: List[str]) -> None:
        """
        Write a function that reverses a string.
        The input string is given as an array of characters s.
        Do not return anything, modify s in-place instead.
        """
        stringlength=len(s)
        s[:stringlength:1] = s[stringlength::-1]