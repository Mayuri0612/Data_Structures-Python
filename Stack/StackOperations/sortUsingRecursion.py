# Reversing of stack using recursions
def insertStack(stack, item): 
    if isEmpty(stack) or item > stack[-1]:
        push(stack, item) 
    else:
        temp = pop(stack) 
        insertStack(stack, item) 
        push(stack, temp) 
  
def sortStack(stack): 
    if not isEmpty(stack): 
        temp = pop(stack)
        sortStack(stack) 
        print(temp)
        insertStack(stack, temp) 
  
def createStack(): 
    stack = [] 
    return stack 
  

def isEmpty( stack ): 
    return len(stack) == 0
  

def push( stack, item ): 
    stack.append( item ) 
  

def pop( stack ):    
    if(isEmpty( stack )): 
        print("Stack Underflow ") 
        exit(1)   
    return stack.pop() 
  
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
  
# Driver Code 
  
stack = createStack() 
push( stack, -30 ) 
push( stack,  -40)
push( stack, -12 ) 
push( stack, -20) 
print("Original Stack ") 
prints(stack) 
  
sortStack(stack) 
  
print("\nReversed Stack ") 
prints(stack) 