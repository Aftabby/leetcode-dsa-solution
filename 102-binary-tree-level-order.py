"""
problem_name = Binary Tree Level Order Traversal
problem_source = https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Algo 
    -
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            temp = list()
            for _ in range(len(queue)):
                if queue[0].left:           # Or here, you can use: " queue.extend([child for child in (node.left, node.right) if child]) "
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                temp.append(queue.pop(0).val)
            result.append(temp)
        return result
