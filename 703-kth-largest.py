'''
problem_name = Kth Largest Element in a Stream
problem_source = https://leetcode.com/problems/kth-largest-element-in-a-stream/

Algo 
    -
'''

from typing import List, Optional


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        ...
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


#TEST
solve = KthLargest(3,[4,5,8,2])

print(solve.add(3))
print(solve.add(5))
print(solve.add(10))
print(solve.add(9))
print(solve.add(4))