
'''
project_name = Binary Tree Inorder Traversal

problem_statement = Given the root of a binary tree, return the inorder traversal of its nodes' values.

problem_source = https://leetcode.com/problems/binary-tree-inorder-traversal/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= [1,null,2,3]
example1_output= [1,3,2]

example2_input= []
example2_output= []

examplen_input= [1]
examplen_output= [1]

steps-
    Implement the solution and test it using example input, check it results the correct output. Fix bugs, if any
    Analyze trhe algorithms complexity and identity inefficiencies, if any
    Apply the right technique to overcome the inefficiencies, then repeat the steps again
    State the most correct and efficient solution in plain english
'''

'''
Algo
    - 
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        return list(self.helper(root))
    
    def helper(self, root):
        if root is not None:
            if root.left is not None:
                yield from self.helper(root.left)
            yield root.val
            if root.right is not None:
                yield from self.helper(root.right)
            
