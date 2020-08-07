
class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;
    
class cllcreate:
    def __init__(self):
        self.head = Node(None);
        self.tail = Node(None);
        self.head.next = self.tail;
        self.tail.next = self.head;

    def add(self, data):
        new_node = Node(data);
        if self.head.data is None:
            self.head = new_node;
            self.tail = new_node;
            new_node.next = self.head;
        else:
            self.tail.next = new_node;
            self.tail = new_node;
            self.tail.next = self.head;

    def display(self):
        temp = self.head;
        if self.head is None:
            print("list is empty");
            return;
        else:
            print('Nodes of circular linked list')
            print(temp.data);
            while(temp.next != self.head):
                temp = temp.next;
                print(temp.data);

class CircularLinkedList:
    cll = cllcreate();
    cll.add(1);
    cll.add(2);
    cll.add(3);
    cll.add(4);
    cll.display();

