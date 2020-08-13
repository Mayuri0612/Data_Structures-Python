# Circular Queue implementation using Arrays.
class Queue:
    def __init__(self, cap):
        self.tail = -1
        self.head = -1
        #self.size = 0
        self.cap = cap
        self.arr = [None] * cap

    def IsEmpty(self):
        return (self.tail == -1)


    def isFull(self):
        return (self.head  == (self.tail + 1) % self.cap)


    def Enqueue(self, data):
        if self.isFull():
            print("Overflow Condition")
            return
        elif self.IsEmpty():
            self.tail = self.head = 0
            self.arr[self.tail] = data
            print("Enqueued item is : " + str(data))
        else:
            self.tail = (self.tail + 1) % self.cap
            self.arr[self.tail] = data
            print("Enqueued item is : " + str(data))
        print("Location of head is : " + str(self.head))
        print("Location of tail is : " + str(self.tail))



    def Dequeue(self):
        if self.IsEmpty():
            print("Queue is Empty")
        elif(self.head == self.tail):
            temp = self.arr[self.head]
            self.head = self.tail = -1
            print("Dequeued element is : " + str(temp))

        else:
            temp = self.arr[self.head]
            self.head = (self.head + 1) % self.cap
            print(" Dequeued element is : " + str(temp))
        print("Location of head is : " + str(self.head))
        print("Location of tail is : " + str(self.tail))

if __name__ == "__main__":
    #capacity = int(input())
    q = Queue(5)
    #array = [q.Enqueue(i) for i in input().split()][:capacity]
    q.Enqueue(1)
    q.Enqueue(2)
    #q.Dequeue() #1
    q.Enqueue(3) 
    q.Enqueue(4)
    #q.Dequeue() #2
    q.Enqueue(5)
    q.Dequeue()
    q.Enqueue(6)


