
'''
project_name = Remove Element

problem_statement = Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

problem_source = https://leetcode.com/problems/remove-element/


problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= nums = [3,2,2,3], val = 3
example1_output= 2, nums = [2,2,_,_]

example2_input= nums = [0,1,2,2,3,0,4,2], val = 2
example2_output= 5, nums = [0,1,4,0,3,_,_,_]

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
    - For the array we will use two pointer, one for each of elements of the array (current) and another to insert the elements that are not equal to val(other) i.e next non val position or index
    - In each iteration, if the current element matches with the val, increment current, if doesn't match, assign the current pointer to the other pointer and increment both the pointer
'''


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        other = 0
        for current in range(len(nums)):
            if nums[current] != val:
                nums[other] = nums[current]
                other += 1
        return other