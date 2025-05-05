'''
problem_name = Subsets
problem_source = https://leetcode.com/problems/subsets/description/

Algo 
    - Start with empty subset [[]]
    - For each value of the input list, add the value with each of the existing subset value and append the new values in the subset
    - You'll get the proper subset of the input list
'''


from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for num in nums:
            for result in results.copy():       #results.copy() - otherwise the loops will go on forever, because we are appending in each iteration
                results.append(result + [num])
        return results