class myStack:                 #creating a blueprint of any objects of type stack and defining the operations that myStack will be able to do
    def __init__(self):        #Define init method for the stack which is the constructor. Methods start with a parameter called self
            self.items = []    #Items is a method member of stack
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def push(self, item):
        #Push the elements at the last index
        self.items.append(item)
         
    def pop(self):
        if self.isEmpty is True:
            return None
        else:
            return self.items.pop()
        
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
        
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
        
    def show(self):
        return self.items
         

s = myStack()  #Create an object s of the type Stack Array(myStack)
s.push('10')
s.push('20')
print("Stack: ",s.items)
print("Size of Stack:",s.size())
print("Is Stack Empty?",s.isEmpty())
print("Popped element:",s.pop())     #It pops the last element because stack is of LIFO structure
print("Stack:",s.show())