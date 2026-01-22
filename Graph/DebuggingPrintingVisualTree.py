class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def print_tree_visual(node, level=0):
    if node is not None:
        # Print right child first (so it appears at the top)
        print_tree_visual(node.right, level + 1)
        
        # Print current node with indentation
        print(' ' * 4 * level + '-> ' + str(node.val))
        
        # Print left child
        print_tree_visual(node.left, level + 1)

# Using your setup from before:
val1 = TreeNode(1)
val1.left, val1.right = TreeNode(2), TreeNode(3)
val1.left.left, val1.left.right = TreeNode(4), TreeNode(5)
val1.right.left, val1.right.right = TreeNode(6), TreeNode(7)

print_tree_visual(val1)