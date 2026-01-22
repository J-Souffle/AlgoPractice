class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    # recursion
def dfs_recursive(node):
    # base case
    if not node:
        return

    # process current node
    print(node.val)

    dfs_recursive(node.right)
    dfs_recursive(node.left)

val1 = TreeNode(1)
val1.left = TreeNode(2)
val1.right = TreeNode(3)
val1.left.left, val1.left.right = TreeNode(4), TreeNode(5)
val1.right.left, val1.right.right = TreeNode(6), TreeNode(7)

#       1
#     /   \
#    2     3
#  /  \   /  \
# 4   5  6    7
 
print(dfs_recursive(val1))

