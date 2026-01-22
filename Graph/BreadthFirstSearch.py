from collections import deque 
# always import this for bfs ^^^

class TreeNode:
    def __init__(self, value):
        self.node = value
        self.left = None
        self.right = None
    
    # use a queue
    def bfs(self):
        # 1. Initialize the queue with the root (self)
        queue = deque([self])
        result = []

        # loop until queue is empty
        while queue:
            # pop the oldest node (left side of dequeue)
            current = queue.popleft
            result.append(current.val)

            # add children to the back of the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        return result

            

    
    # def printTree(self, node):
        
        


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

print(val1.bfs())