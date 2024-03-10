class Solution:
    def postorderTraversal(self, root) -> list[int]:
        return list(self.helper(root))
    
    def helper(self, root):
        if root is not None:
            if root.left is not None:
                yield from self.helper(root.left)
            if root.right is not None:
                yield from self.helper(root.right)
            yield root.val
            