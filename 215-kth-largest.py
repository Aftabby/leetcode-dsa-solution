'''
problem_name = Kth Largest Element in an Array
problem_source = https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Algo 
    -
'''
from typing import Optional, List
import random

#Applying quick sort method

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        small, equal, large = list(), list(), list()        

        for i in nums:
            if i < pivot:
                small.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                large.append(i)
        
        if len(large) >= k:
            return self.findKthLargest(large, k)    #k-th largest number is in the largest part
        elif (len(equal) + len(large)) >= k:
            return pivot                            #k-th largest number is equal to the pivot
        else:
            return  self.findKthLargest(small, k-len(large)-len(equal)) #k-th largest number is in the smallest part
        



