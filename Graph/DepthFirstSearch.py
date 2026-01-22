class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
    # recursion
    def dfs_recursive(self, node):
        # base case
        if not node:
            return

        # process current node
        print(node.val)

        dfs_recursive(node.right)
        dfs_recursive(node.left)

