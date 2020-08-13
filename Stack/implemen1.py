# Stack implementation in python

class Stack:
    def __init__(self, cap):
        self.top = -1
        self.cap = cap
        self.stack = [None] * cap

    def check_empty(self):
        return self.top == -1

    def isFull(self):
        return(self.top == self.cap - 1)

    def push(self, item):
        if self.isFull():
            print("Stack overflow")
        try:
            self.stack[self.top + 1] = item
            self.top += 1
            print("pushed item: " + str(item))
        except IndexError:
            print("You are entering more elements than capacity")

        

    def pop(self):
        if (self.check_empty()):
            print("Stack underflow")
        popped = self.stack.pop()
        print("popped item : " + str(popped))
        self.top -= 1



capacity = int(input())
s = Stack(capacity)
array = [s.push(i) for i in input().split()][:capacity]
s.pop() 
#s.push('6')
print("New stack : " + str(s.stack))
