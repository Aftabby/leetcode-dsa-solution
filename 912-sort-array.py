"""
problem_name = Sort an Array
problem_source = https://leetcode.com/problems/sort-an-array/description/

Algo 
    -

"""
#Insertion Sort - O(n^2)
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for index in range(1, len(nums)):
            for curr in range(index, 0, -1):
                if nums[curr] >= nums[curr-1]:
                    break
                else:
                    nums[curr], nums[curr-1] = nums[curr-1], nums[curr]

        return nums








#Selection Sorting algo - O(n^2)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        for index in range(len(nums)):
            min_index = index
            for check in range(index+1, len(nums)):
                if nums[min_index] > nums[check]:
                     min_index = check
            nums[min_index], nums[index] = nums[index], nums[min_index]
        return nums
    




# Merge Sort
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(low, mid, high):
            first_half = nums[low : mid + 1]
            second_half = nums[mid + 1 : high + 1]
            first_pointer = 0
            second_pointer = 0

            for _ in range(low, high + 1):
                if not (second_pointer < len(second_half)) or (
                    first_pointer < len(first_half)
                    and first_half[first_pointer] <= second_half[second_pointer]
                ):
                    nums[_] = first_half[first_pointer]
                    first_pointer += 1
                elif second_pointer < len(second_half):
                    nums[_] = second_half[second_pointer]
                    second_pointer += 1

        def mergeSort(low, high):
            if low < high:
                mid = int((low + high) / 2)

                mergeSort(low, mid)
                mergeSort(mid + 1, high)  # 2nd half

                merge(low, mid, high)

        mergeSort(0, len(nums) - 1)
        return nums


nums = [5, 2, 3, 1]

solve = Solution()
result = solve.sortArray(nums)
