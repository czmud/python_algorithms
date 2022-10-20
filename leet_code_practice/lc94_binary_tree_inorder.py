# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# quick recursive binary tree traversal
class Solution:
    def __init__(self):
        self.result_list = []
    def inorderTraversal(self, root):
        if not root:
            return
        
        if root.left != None:
            self.inorderTraversal(root.left)
        if root.val != None:
            self.result_list.append(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)
            
        return self.result_list