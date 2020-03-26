class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            print('empty')
        
        else:
            old_top = self.top
            new_top = self.top.next
            self.top = new_top
            self.length -= 1
            return old_top.value


    def print_data(self):
        if self.length == 0:
            print('Already empty')
        current = self.top
        while current:
            print(current.value, self.length)
            current = current.next

    

my_stack = Stack()
# print(my_stack.peek())
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_data()
my_stack.pop()
my_stack.pop()
my_stack.print_data()
my_stack.pop()
print('is it empty?')
my_stack.print_data()