
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        shuffle = list()
        for x in range(n):
            shuffle.append(nums[x]) 
            shuffle.append(nums[n])
            n += 1
        return shuffle


#Another approach
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return [elements for x in range(n) for elements in [nums[x], nums[n + x]]]




test = Solution()

assert test.shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
assert test.shuffle([1,2,3,4,4,3,2,1], 4) == [1,4,2,3,3,2,4,1]








'''
problem_name = Shuffle the Array
problem_source = https://leetcode.com/problems/shuffle-the-array/description/

Algo 
    -
    -

    2nd one
    -Define a function called shuffle that takes two parameters: a list of integers nums and an integer n.
    -Inside the function, return a new list that is created by the following process:
        -Iterate over each index from 0 to n-1 (inclusive). For each index, do the following:
            -Add the element at the current index from the list nums to the new list.
            -Add the element at the index of current index plus one from the list nums to the new list.
    -This algorithm essentially interleaves the first n elements and the second n elements of the list nums.
'''