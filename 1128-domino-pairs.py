from typing import List

# @ DIDN'T SOLVE
"""
problem_name = Number of Equivalent Domino Pairs
problem_source = https://leetcode.com/problems/number-of-equivalent-domino-pairs/?envType=daily-question&envId=2025-05-04

Algo
    -
"""
# @ DIDN'T SOLVE
# @ DIDN'T SOLVE
# @ DIDN'T SOLVE


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        count = 0
        freq = {}
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            freq[key] = freq.get(key, 0) + 1

        for v in freq.values():
            count += v * (v - 1) // 2

        return count"""


# Test cases
