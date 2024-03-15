
'''
project_name = Remove Duplicates from Sorted Array

problem_statement = Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

problem_source = https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= nums = [1,1,2]
example1_output= 2, nums = [1,2,_]

example2_input= nums = [0,0,1,1,1,2,2,3,3,4]
example2_output= 5, nums = [0,1,2,3,4,_,_,_,_,_]

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
    - We have set two pointers, one for each of the last unique values, one for the each of current element of the node(except first one)
    - If the current element and the last unique value matches (i.e duplicate), we increment the current element by 1 to find the next unique number
    - If the current element and the last unique value doesn't match (i.e unique), we assign the current element after the last unique value, and update the last unique value and continue the process for the remaining elements
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        unique = 0     #The pointer for unique values

        for current in range(1, length):    #The pointer for each elements
            if nums[unique] != nums[current]:
                unique += 1
                nums[unique] = nums[current]

        return unique+1
            