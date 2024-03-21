"""
problem_name = Fibonacci Number
problem_source = https://leetcode.com/problems/fibonacci-number/description/

Algo 
    -
"""

#Recursion Approach
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)


#Iterative Approach
class Solution:
    def fib(self, n: int) -> int:
        y = 1
        x = 0
        sum = 0
        for _ in range(n-1):
            sum = x + y
            x = y
            y = sum
        return sum if n > 1 else y if n else x
    


#Memoization approach - using cache decorator
from functools import cache

class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)