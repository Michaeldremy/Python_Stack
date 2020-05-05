# Stack is a last in, first out data structure.

# We can use a Singly Linked List as a stack

# Insert into a stack (push) is the same as Adding to the front of a SLL

# Removing from a stack (pop) is the same as Removing from the front of a SLL

# The goal is to use what we know about SLL to build a Stack with the following methods
class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def Push(self,val):
        newnode = SLNode(val)
        if(self.head == None):
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        return self

    def Pop(self):
        poppedval = self.head.value
        self.head = self.head.next
        print(poppedval)
        return self

    def Peek(self):
        peekedval = self.head.value
        print(peekedval)
        return self

    def StackDisplay(self):
        runner = self.head
        while runner!=None:
            print(str(runner.value) + "->")
            runner = runner.next
        return self

s1 = Stack()
s1.Push(10)
s1.Push(20)
s1.Push(30)
s1.StackDisplay()
s1.Peek()
s1.Pop()
s1.Peek()