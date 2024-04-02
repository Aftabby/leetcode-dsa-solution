"""
problem_name = Construct Binary Tree from Preorder and Inorder Traversal
problem_source = https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Algo 
    - In Pre Order the first element is the root, Then we can find the first element in the InOrder list, All element in the inorder list in the left of the root element is its left subtree and vice versa
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:  # That is no root left or no child left
            return
        root = preorder[0]  # The first element of the preorder is the root
        root_index = inorder.index(root)  # Finding the root-index in the inorder list
        preorder.remove(root)

        binary_tree = TreeNode(
            root
        )  # Creating a binary tree with the node, where the value is the root, the left subtree is the "all the left elements of the root element in the inorder list" and vice versa for the right subtree

        if inorder[:root_index]:
            binary_tree.left = self.buildTree(
                preorder, inorder[:root_index]
            )  # Checking if left branch exists or not, and then assigning
        if inorder[root_index + 1 :]:

            binary_tree.right = self.buildTree(
                preorder, inorder[root_index + 1 :]
            )  # Checking if right branch exists or not, and then assigning

        return binary_tree


# TESTS
inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]

solve = Solution()
result = solve.buildTree(inorder=inorder, preorder=preorder)
print(result.val)

inorder = [1, 2]
preorder = [1, 2]

result = solve.buildTree(inorder=inorder, preorder=preorder)

inorder = [1, 2, 3, 4]
preorder = [3, 1, 2, 4]

result = solve.buildTree(inorder=inorder, preorder=preorder)
