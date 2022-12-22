from collections import deque
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        node_queue = deque([(p, q)])

        while node_queue:
            (next_p, next_q) = node_queue.popleft()

            if not next_p and not next_q:
                continue
            
            if not next_p or not next_q or next_p.val != next_q.val:
                return False

            node_queue.append((next_p.left, next_q.left))
            node_queue.append((next_p.right, next_q.right))
        
        return True
    
    # encode binary tree as string, then use string comparison to determine tree equivalence
    def isSameTreeStringify(self, p, q):
        p_string = generateString(p)
        q_string = generateString(q)

        return True if p_string == q_string else False

# encode empty nodes as "_"
def generateString(root):
    if not root:
        return "_"
    
    res_string = str(root.val)
    res_string += generateString(root.left)
    res_string += generateString(root.right)
    
    return res_string