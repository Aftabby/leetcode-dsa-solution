'''
problem_name = Delete Node in a BST
problem_source = https://leetcode.com/problems/delete-node-in-a-bst/description/

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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #Helper function - to find the minimum valuse from a subt
        def find_min_node(root: Optional[TreeNode]):
            while root.left:
                root = root.left
            return root


        #If no tree
        if not root:
            return root

        head = prev = root

        #Search of the node to delete
        while root and root.val != key:
            prev = root
            if root.val > key:
                root = root.left
            else:
                root = root.right
        
        #Deleting the node
        if not root:        #The node does not exist
            return head     
        else:               #The node exist
            if not (root.left and root.right):              # Case 1 : If the node has 0 or 1 child 
                if root.val < prev.val:                         #Checking Which child is the deleting node of its ancestor
                    if not root.left:
                        prev.left = root.right
                    else:
                        prev.left = root. left
                elif root.val == prev.val:                  #Only when the root node (whic has 1 or 0 child) has to be deleted this block will execute, this block will execute
                    return root.right if root.right else root.left
                else:
                    if not root.left:
                        prev.right = root.right
                    else:
                        prev.right = root.left
            else:                                           # Case 2 : If the node has both the child
                min_right_child = find_min_node(root.right)     #Getting the minimum value from the right sub-tree
                head = self.deleteNode(head, min_right_child.val)   #Deleting that min value using recursive method
                root.val = min_right_child.val                      #Replacing the deleting value with min value from right sub-tree
        return head
    




#Try using Recursive approach