# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solves 93/94 test cases - times out on last case
# too many repeated tests of nodes
# should update so as to not call "maxChildPath" function so much
# this is something like an O(n^2) solution
class Solution:
    def maxPathSum(self, root):
        return_max = root.val
        
        #test all nodes as possible pivot point for largest path
        node_stack = [root]
        while node_stack:
            next_node = node_stack.pop()
            return_max = max(return_max, self.possiblePivot(next_node))
            if next_node.left:
                node_stack.append(next_node.left)
            if next_node.right:
                node_stack.append(next_node.right)
        
        return return_max
    
    def possiblePivot(self, node):
        left_path = 0
        right_path = 0
        
        if node.left:
            left_path = self.maxChildPath(node.left)
        if node.right:
            right_path = self.maxChildPath(node.right)
            
        return left_path + node.val + right_path
    
    def maxChildPath(self, node):
        left_path = 0
        right_path = 0
        
        if node.left:
            left_path = max(0, self.maxChildPath(node.left))
        if node.right:
            right_path = max(0, self.maxChildPath(node.right))
            
        return max(0, max(right_path, left_path) + node.val)

class Solution2:
    def __init__(self):
        self.node_map = {}
    def maxPathSum(self, root):
        return_max = root.val
        
        #test all nodes
        node_stack = [root]
        while node_stack:
            next_node = node_stack.pop()
            return_max = max(return_max, self.possiblePivot(next_node))
            if next_node.left:
                node_stack.append(next_node.left)
            if next_node.right:
                node_stack.append(next_node.right)
        
        return return_max
    
    def possiblePivot(self, node):
        left_path = 0
        right_path = 0
        
        if node.left:
            left_path = self.maxChildPath(node.left)
        if node.right:
            right_path = self.maxChildPath(node.right)
            
        return left_path + node.val + right_path
    
    def maxChildPath(self, node):
        if id(node) not in self.node_map:
            left_path = 0
            right_path = 0

            if node.left:
                left_path = max(0, self.maxChildPath(node.left))
            if node.right:
                right_path = max(0, self.maxChildPath(node.right))
            
            self.node_map[id(node)] = max(0, max(right_path, left_path) + node.val)    
        
        return self.node_map[id(node)]

class Solution3:
    def __init__(self):
        self.max_path
    def maxPathSum(self, root):
        self.max_path = root.val
        
        self.testNodeAsMax(root)
        return self.max_path
    
    def testNodeAsMax(self, node):
        if not node:
            return 0
        left_path = max(0, self.testNodeAsMax(node.left))
        right_path = max(0, self.testNodeAsMax(node.left))

        self.max_path = max(self.max_path, left_path + node.val + right_path)
        return max(left_path, right_path)
