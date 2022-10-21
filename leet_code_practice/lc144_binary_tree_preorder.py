class Solution:
    def __init__(self):
        self.result_list = []
    def preorderTraversal(self, root):
        if not root:
            return
        
        if root.val != None:
            self.result_list.append(root.val)
        if root.left != None:
            self.preorderTraversal(root.left)
        if root.right != None:
            self.preorderTraversal(root.right)
            
        return self.result_list