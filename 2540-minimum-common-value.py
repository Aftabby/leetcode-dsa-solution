
'''
project_name = Minimum Common Value

problem_statement = Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
                    Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

problem_source = https://leetcode.com/problems/minimum-common-value/description/?envType=daily-question&envId=2024-03-10

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= nums1 = [1,2,3], nums2 = [2,4]
example1_output= 2

example2_input= nums1 = [1,2,3,6], nums2 = [2,3,4,5]
example2_output= 2

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
    - Set two pointer at the start of each of the list
    - Compare the two pointer, if equal return the num
    - if not equal, increase the pointer by 1 of the smallest value's list
    - Repeat from step 2 until one of list is out of pointer (index)
    - return -1
'''


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        pointer1, pointer2 = 0, 0
        len1, len2 = len(nums1), len(nums2)

        while pointer1 < len1 and pointer2 < len2:
            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1
            else:
                return nums1[pointer1]
        return -1


solve = Solution()
result1 = solve.getCommon(nums1 = [1,2,3,6], nums2 = [2,3,4,5])
result2 = solve.getCommon(nums1 = [1,2,3], nums2 = [2,4])

print(result1, result2)
