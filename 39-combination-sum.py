"""
problem_name = Combination Sum
problem_source = https://leetcode.com/problems/combination-sum/description/

Algo 
    - Backtracking
    - First we reversed the candidates list, the for each of the value we took all the combination of the list elements (including itself and in repetitive manner)
    - When the sum of the combination (temp) is greater than our target we popped last element and started combining with the next element
    - When the sum of the combination is less than our target we added up the same element (with which element we were working on that time)
    - Else when the sum is equal to the target we added the combination to the final list (results)
    - Though this method doesn't show correct output in the edge cases
"""

from typing import List


# THIS METHOD IS NOT WORKING IN EDGE CASES
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def find_combination():
            nonlocal candidates
            candidates = list(reversed(candidates))       #Converting from ascending to descending, The reversed() function in Python doesn't actually return a list, but rather an iterable object of type reversed
            length = len(candidates)
            results = list()        #This is the returned result list

            for index, candidate in enumerate(candidates):  #For each of the element in the candidates list, in descending order
                temp = list()
                while index < length:
                    if sum(temp) < target:              #When the total sum is less than the target
                        temp.append(candidates[index])
                    elif sum(temp) > target:            #When the total sum is greater than the target
                        temp.pop()
                        index += 1
                    else:                               #When the total sum equal to the the target
                        results.append(temp.copy())     #Not appending the the reference of the list -- temp -- rather a copy(or snapshot) so that later changing the temp list won't affect the --results-- variable
                        index += 1
                        temp.pop()
            return results

        return find_combination()






#Alternative Approach


class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def dfs(s, target, path):
      if target < 0:
        return
      if target == 0:
        ans.append(path.clone())
        return

      for i in range(s, len(candidates)):
        path.append(candidates[i])
        dfs(i, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans









#Tests
solve = Solution()
result = solve.combinationSum([2,3,6, 7], 7)
print(result)