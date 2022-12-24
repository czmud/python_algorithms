class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        res_max_depth = 1
        res_max_depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        return res_max_depth