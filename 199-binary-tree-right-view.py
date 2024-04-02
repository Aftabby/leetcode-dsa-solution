"""
problem_name = Binary Tree Right Side View
problem_source = https://leetcode.com/problems/binary-tree-right-side-view/description/

Algo 
    - For each level of BFS we are taking the last element of the level and appending it to to 'res' list
    - At last returning the 'res' list
    
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        res = list()
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                queue.extend(
                    [child for child in (queue[0].left, queue[0].right) if child]
                )
                queue.pop(0)
        return res
