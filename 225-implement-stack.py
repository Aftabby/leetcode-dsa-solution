"""
problem_name = Implement Stack using Queues
problem_source = https://leetcode.com/problems/implement-stack-using-queues/

Algo 
    -
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.list = list()

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        return self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def empty(self) -> bool:
        return False if self.list else True


# Another approach - using dequeue
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return False if self.queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
