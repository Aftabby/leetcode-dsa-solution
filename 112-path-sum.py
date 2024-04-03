"""
problem_name = Path Sum
problem_source = https://leetcode.com/problems/path-sum/description/

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


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, path=0) -> bool:
        if root is None:
            return

        path += root.val

        if not root.left and not root.right:
            return path == targetSum

        return self.hasPathSum(root.left, targetSum, path) or self.hasPathSum(
            root.right, targetSum, path
        )
