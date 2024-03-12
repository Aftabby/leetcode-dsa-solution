
'''
project_name = Maximum Depth of Binary Tree

problem_statement = Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

problem_source = https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= [3,9,20,null,null,15,7]
example1_output= 3

example2_input= [1,null,2]
example2_output= 2

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
    RECURSION
    - First we check the node is None or not, if None return 0 
    - else call the same function passing root.left and root.right 
    - then return the value of which one is the max
    - It's a DFS method

    ITERATION
    - if root is not a TreeNode, return 0
    - else append the root to queue list
    -Till queue is not empty
        -Iterate over each elements of queue(which will be parents) and append each valid child element of the current element
        -Remove the parent elements and increment the depth variable by 1

'''


from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS - Recureion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


#BFS - Iteration Method
class Solution:
    def maxDepth(self, root):
        if not isinstance(root, TreeNode):
            return 0
        queue, depth_count = [root], 0
        while queue:
            length = len(queue)
            for i in range(0, length):
                node = queue[i]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            depth_count += 1 
            queue[0: length] = []
            
        return depth_count





