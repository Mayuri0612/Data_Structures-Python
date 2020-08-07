class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    h = height(root)
    for i in reversed(range(1,h+1)):
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