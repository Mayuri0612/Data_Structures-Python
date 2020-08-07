'''
Insertion in binary search tree
'''

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

if if __name__ == "__main__":
    r = Node(50) 
    insert(r,Node(30)) 
    insert(r,Node(20)) 
    insert(r,Node(40)) 
    insert(r,Node(70)) 
    insert(r,Node(60)) 
    insert(r,Node(80)) 