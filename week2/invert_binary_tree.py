class Solution:    
    def invertTree(self, root: TreeNode) -> TreeNode:
        # If empty tree, return nothing
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root