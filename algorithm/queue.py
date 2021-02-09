# FIFO First In First Out
class Queue:
    def __init(self):
        self.queue = []

    #O(1)
    def is_empty(self):
        return self.queue == []
    
    #O(1)
    def enqueue(self, data):
        self.queue.append(data)

    #O(1)
    def dequeue(self):
        data =self.queue[0]
        del self.queue[0]
        return data
    
    #O(1)
    def peek(self):
        return self.queue[0]

    #O(1)
    def size_queue(self):
        return len(self.queue)