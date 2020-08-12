# Array implementation of queue
class Queue:
    def __init__(self, cap):
        self.head =  self.size = 0
        self.tail = -1
        self.cap = cap
        self.arr = [None] * cap
    def isFull(self):
        return (self.size == self.cap)
    def isEmpty(self):
        return (self.size == 0)
    def Enqueue(self, data):
        if self.isFull():
            print("Overflow condition")
            return
        else:
            self.tail = (self.tail + 1) % (self.cap)
            self.arr[self.tail] = data
            self.size += 1
            print("Enqueued item : " + str(data))

    def Dequeue(self):
        if self.isEmpty():
            print("Undrflow condition")
            return
        else:
            #removed = self.arr[self.head]
            print("Dequeued item is : " + str(self.arr[self.head]))
            self.head = (self.head + 1) % (self.cap)
            self.size -= 1

if __name__ == "__main__":
    
    capacity = int(input())
    q = Queue(capacity)
    array = [q.Enqueue(i) for i in input().split()][:capacity]
    q.Dequeue() 
    '''
    queue = Queue(40) 
    queue.Enqueue(10) 
    queue.Enqueue(20) 
    queue.Enqueue(30) 
    queue.Enqueue(40) 
    queue.Dequeue() 
    '''



