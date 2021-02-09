# The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity. We can use O(N) extra memory!

# Hint: we can use another stack to track the max item!

class MaxStack:

    def __init__(self):
        #use one stack for enqueue operation
        self.main_stack = []
        #use another stack for dequeue operation
        self.max_stack = []

    #adding an item to the queue is O(1)
    def push(self, data):
        #push the new item onto the the stack
        self.main_stack.append(data)

        #first itemis the same in both stacks
        if(len(self.main_stack)==1):
            self.max_stack.append(data)
            return
        
        #if the item is the largest one so far: we insert it onto the  satack
        #stack[-1] is the peek operation: returns the last item wehave inserted(without removing)
        if data>self.main_stack[-1]:
            self.main_stack.append(data)
        else:
            self.main_stack.append(self.main_stack[-1])

    
    #getting items
    def pop(self):
        self.main_stack.pop()
        return self.main_stack.pop()

    #maxitem isthe last item we have inserted into  the maxStack O(1)
    def get_max_item(self):
        return self.main_stack.pop()

