
'''
project_name = Count Pairs Whose Sum is Less than Target

problem_statement = Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j)
                     where 0 <= i < j < n and nums[i] + nums[j] < target.

problem_source = https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= nums = [-1,1,2,3,1], target = 2
example1_output= 3

example2_input= nums = [-6,2,5,-2,-7,-1,3], target = -2
example2_output= 10

examplen_input= 
examplen_output= 

steps-
    Implement the solution and test it using example input, check it results the correct output. Fix bugs, if any
    Analyze trhe algorithms complexity and identity inefficiencies, if any
    Apply the right technique to overcome the inefficiencies, then repeat the steps again
    State the most correct and efficient solution in plain english (in Algo)
'''

'''
Algo
    - Sorting the list in an ascending order
    For each element in the array, use binary search to find the largest index that makes the sum of the current element and the element at the index less than the target.
The number of pairs for the current element is the index found in step 2 minus the current index.
Sum up the number of pairs for all elements.

'''


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        sum = 0
        length = len(nums)-1

        for i in range(0, length):
            lo = i+1
            hi = length

            if nums[i] + nums[lo] >= target :
                break

            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] + nums[i] < target:
                    lo = mid+1
                else:
                    hi = mid-1
                    lo -= 1
                
            sum += mid-i 
        return sum


hello = Solution()
print(hello.countPairs([-5,-4,-10,7], 14))

    