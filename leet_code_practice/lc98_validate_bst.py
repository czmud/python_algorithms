class Solution:
    def isValidBST(self, root):
        return isValidBSTRecursive(root)


def isValidBSTRecursive(root, memo=[]):
    if not root:
        return True
    
    for test_type, parent_val in memo:
        match test_type:
            case "l":
                if root.val >= parent_val:
                    return False
            case "r":
                if root.val <= parent_val:
                    return False

    left_memo = memo + [("l", root.val)]
    right_memo = memo + [("r", root.val)]

    return isValidBSTRecursive(root.left, left_memo) and isValidBSTRecursive(root.right, right_memo)