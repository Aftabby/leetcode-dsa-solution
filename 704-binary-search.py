
'''
project_name = 704. Binary Search

problem_statement = Given an array of integers nums which is sorted in ascending order, and an integer target, 
                    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
                    You must write an algorithm with O(log n) runtime complexity.

problem_source = https://leetcode.com/problems/binary-search/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= nums = [-1,0,3,5,9,12], target = 9
example1_output= 4

example2_input= nums = [-1,0,3,5,9,12], target = 2
example2_output= -1

examplen_input= 
examplen_output= 

steps-
    Implement the solution and test it using example input, check it results the correct output. Fix bugs, if any
    Analyze trhe algorithms complexity and identity inefficiencies, if any
    Apply the right technique to overcome the inefficiencies, then repeat the steps again
    State the most correct and efficient solution in plain english
'''

'''
Algo
    - Define the higher and lower bound
    - set the mid bound by low + high // 2
    - if mid == num, return mid, else if (mid > num ) set high = mid-1, else if (mid < num) set low = mid+1
    - 
'''


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo<=hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
        return -1

            
