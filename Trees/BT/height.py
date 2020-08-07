class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
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
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(height(root))
