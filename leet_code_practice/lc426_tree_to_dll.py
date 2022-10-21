from datastructures.bst import Node

def treeToDoublyList(root):
    # handle empty bst edge case
    if not root:
        return

    # flatten left side
    lefty = root
    while lefty.left:
        if lefty.left.right:
            bottom = lefty.left.right
            while bottom.left:
                bottom = bottom.left
            bottom.left = lefty.left
            lefty.left = lefty.left.right
            bottom.left.right = None
        else:
            lefty.left.right = lefty
            lefty = lefty.left

    # flatten right side
    righty = root
    while righty.right:
        if righty.right.left:
            bottom = righty.right.left
            while bottom.right:
                bottom = bottom.right
            bottom.right = righty.right
            righty.right = righty.right.left
            bottom.right.left = None
        else:
            righty.right.left = righty
            righty = righty.right

    # add pointers to turn DLL -> circular DLL
    lefty.left = righty
    righty.right = lefty

    # return lefty pointer as it will be the smallest node value
    return lefty



bst1 = Node(4, Node(2, Node(1), Node(3)), Node(5))

print(treeToDoublyList(None))

dll = treeToDoublyList(bst1)


runner = dll
i = 0
while runner.val < runner.right.val:
    print(f'node {i}: {runner.val}')
    runner = runner.right
    i += 1
print(f'node {i}: {runner.val}')
