'''
problem_name = Baseball Game
problem_source = https://leetcode.com/problems/baseball-game/description/

Algo 
    -
'''


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = list()
        for operation in operations:
            if operation == 'C':
                record.pop()
            elif operation == 'D':
                record.append(record[-1]*2)
            elif operation == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(operation))
        return sum(record)


solve = Solution()

assert solve.calPoints(["5","2","C","D","+"]) == 30
assert solve.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert solve.calPoints(["1","C"]) == 0
