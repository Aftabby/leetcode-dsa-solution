
'''
project_name = Diameter of Binary Tree

problem_statement = Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

problem_source = https://leetcode.com/problems/diameter-of-binary-tree/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= [1,2,3,4,5]
example1_output= 3

example2_input= [1,2]
example2_output= 1

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
    - Passing the root and a list with 0 as value in its 0-th index to a helper function
    - For each node, we check the of its left and right branch, and assign the most lengthy branch of left+right
    - We recursively iterate over each of the nodes using DFS approach
    '''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        list1 = [0]
        self.helper(root, list1)    #Passing the list so that it can be accessed later
        return list1[0]
    
    def helper(self, root, list1):
        if root is None:
            return 0
        left, right = self.helper(root.left, list1), self.helper(root.right, list1)
        if list1[0] < (left + right):   #When the left branch + right branch is greater than the current diameter stored
            list1[0] = left + right
        return max(left, right) + 1 




#Another approach
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self_diameter = 0
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self_diameter = max(self_diameter, left+right)
            return max(left, right) + 1
        dfs(root)
        return self_diameter








#Test
tree = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
    
solve = Solution()
result = solve.diameterOfBinaryTree(tree)
print(result)