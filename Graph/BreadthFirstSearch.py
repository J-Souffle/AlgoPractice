class TreeNode:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None
    
    # Base case : rightmost and last level node, Recursive case: elements still in stack
    def bfs(self, node):
        


val1 = TreeNode(1)
val2 = TreeNode(2)
val3 = TreeNode(3)
val4 = TreeNode(4)
val5 = TreeNode(5)
val6 = TreeNode(6)
val7 = TreeNode(7)

val1.left = val2
val1.right = val3
val2.left = val4
val2.right = val5
val3.right = val6
val3.left = val7
        