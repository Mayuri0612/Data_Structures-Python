class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
    
    def isEmpty(self):
        return self.head == None

    def Enqueue(self, item):
        temp = Node(item)
        if self.tail is None:
            self.head = self.tail = temp
        self.tail.next = temp
        self.tail = temp  #tail incremente each time
        print("Enqueued item : " + str(self.tail.data))

    def Dequeue(self):
        if self.isEmpty():
            return
        print("Dequeued data is : " + str(self.head.data))
        temp = self.head
        self.head = temp.next

        if(self.head is None):
            self.tail = None

if __name__ == "__main__":
    
    no_of_nodes = int(input())
    q = Queue()
    array = [q.Enqueue(i) for i in input().split()][:no_of_nodes]
    q.Dequeue() 
        