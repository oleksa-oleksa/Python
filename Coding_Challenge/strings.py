"""
This is LeetCode's official curated list of Top classic interview question

"""


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
