"""
problem_name = Insert into a Binary Search Tree
problem_source = https://leetcode.com/problems/insert-into-a-binary-search-tree/

Algo 
    -
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative Approach
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Checking the BST is empty or not
        if not root:
            return TreeNode(val)
        else:
            head = root

        # Traversing over the BST to find the exact location to insert New value
        while root:
            prev = root
            if root.val > val:
                root = root.left
            else:
                root = root.right

        # Inserting the new value
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        # Returning the head(root)
        return head


# Recursive Approach
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
