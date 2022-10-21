class Solution:
    def __init__(self):
        self.result_list = []
    def postorderTraversal(self, root):
        if not root:
            return
        
        if root.left != None:
            self.postorderTraversal(root.left)
        if root.right != None:
            self.postorderTraversal(root.right)
        if root.val != None:
            self.result_list.append(root.val)
            
        return self.result_list