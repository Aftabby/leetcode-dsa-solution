'''
problem_name = Sort Colors
problem_source = https://leetcode.com/problems/sort-colors/

Algo 
    -
'''

from typing import List

#Using Bucket Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        color_count = {i: 0 for i in range(3)}

        for i in nums:
            color_count[i] += 1
        
        #nums = [val for val in color_count for i in range(color_count[val])]   #If we had to return the list, this is not modifying the list in-place 

        i = 0
        for key in color_count:
            for val in range(color_count[key]):
                nums[i] = key
                i += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        