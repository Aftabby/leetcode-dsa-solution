'''
problem_name = Min Stack
problem_source = https://leetcode.com/problems/min-stack/

Algo 
    -
'''

class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        last = self.stack.pop()
        if last == self.min[-1]:
            self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
