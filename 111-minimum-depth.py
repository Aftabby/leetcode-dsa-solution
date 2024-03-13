
'''
project_name = Minimum Depth of Binary Tree

problem_statement = Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

problem_source = https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

problem_explanation = 
'''

'''
*including edge cases, create test cases for each of the scenerios below*

example1_input= [3,9,20,null,null,15,7]
example1_output= 2

example2_input= [2,null,3,null,4,null,5,null,6]
example2_output= 5

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
    -if the node is leaf, return 1,
    -if it has both the child, call the function again for both the child and return the minimum one(route) +1 (for the node itself)
    -if it has only one child, call the function again with that child only, return the returned value +1 (for the node itself)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
#Finding the minimum depth of a binary tree using recursion
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) +1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) +1
        





class Solution:
#Finding the minimum depth of a binary tree using iteration (BFS)
    def minDepth(self, root) -> int:
        if root is None:
            return 0
        level, depth = [root], 0
        while level:
            length = len(level)
            for i in range(length):
                if level[i].left is None and level[i].right is None:
                    return depth+1
                if level[i].left is not None:
                    level.append(level[i].left)
                if level[i].right is not None:
                    level.append(level[i].right)
            level[:length]=[]
            depth += 1
        
                


#Test
tree = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
    
solve = Solution()
result = solve.minDepth(tree)
print(result)