"""
problem_name = Climbing Stairs
problem_source = https://leetcode.com/problems/climbing-stairs/

Algo 
    # Recursive Approach with memoization
    - For each step ahead there is only two way: Two-steps or one-step
    - Before beginning each step, we have to determine how many steps left for us, if we have no step left (n == 0) return 1    (That is, we are went fully through a path)
                                                    - else we have steps left, call the same function twice with one-step (n -1) and two-steps(n -2)
                                                    - else return 0 (because we have travelled the path that doesn't exits, like n == -1)

    # Dynamic Iterative approach
    - We are defining a list of 3 elements [0, 1, 2], where each of the element's value is its index number. (Why? because the number of index matches with the number of ways to climb the stairs (up to two stairs))
    - If n > 2 : we are iterating over from 3 to n and for each index of the list of that number we are appending the summation of the value of its previous two steps (because n has the same number of ways as the (n-1) ways + (n-2) ways)
    - Returning the n-indexed value  of the list that, because in the n-index we appended the total number of ways for n-steps

    # Fibonacci approach
    - Sum = x + y , for each iteration of n times, we changed the value of x = y and y = sum 
    - For more, see the problem 509-fibonacci-number.py
    
"""

# Recursive Approach with memoization
from functools import cache


class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n > 0:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        else:
            return 0


# Iterative Approach (Dynamic)
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [step for step in range(3)]
        if n > 2:
            for _ in range(3, n + 1):
                steps.append(
                    steps[_ - 1] + steps[_ - 2]
                )  # Or you can also, use seps[i] = the_value istead of append, for that, first declare (steps = [0] * (n + 1))
        return steps[n]


# Fibonacci approach
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 0
        prev1 = 1
        curr = 0
        for _ in range(n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return curr


# Fibonacci Formula approach
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2

        return int((math.pow(phi, n + 1) - math.pow(psi, n + 1)) / sqrt5)
