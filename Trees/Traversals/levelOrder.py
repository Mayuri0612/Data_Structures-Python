'''
# Using Recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        givenLevel(root, i)

def givenLevel(root, level):
    if root is None:
        return 0
    if level == 1:
        print(root.data, end = " ")
    elif level > 1:
        givenLevel(root.left, level-1)
        givenLevel(root.right,level-1 )

    
def height(node):
    if node is None:
        return 0
    else:
        l = height(node.left)
        r = height(node.right)
        if l > r:
            return l+1
        else:
            return r+1

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.right.left = Node(1)
    root.left.right = Node(4)

    levelOrder(root)
'''
# Using Queue Data structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return 0
    
    queue = []
    queue.append(root)
    while(len(queue) > 0):
        print(queue[0].data, end = " ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    root = Node(input())
    root.left = Node(input())
    root.right = Node(input())
    root.right.left = Node(input())
    root.left.right = Node(input())

    levelOrder(root)
