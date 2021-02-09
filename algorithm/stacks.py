#LIFO Last Item First Out

class Stack:
    def __init__(self):
        self.stack = []

    #Insert item into the stack // O(1)
    def push(self, data):
        self.stack.append(data)

    #remove and return the last item we  have inserted // O(1)
    def pop(self):
        if self.stack_size()<1:
            return -1
            
        data = self.stack[-1]
        del self.stack[-1]
        return data

    #peek: it returns the last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    #has  O(1)
    def is_empty(self):
        return self.stack == []
    
    def stack_size(self):
        return len(self.stack)