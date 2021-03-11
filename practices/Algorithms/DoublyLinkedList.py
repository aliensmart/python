# Each node is linked to the next and previous node

class Node:
    def __init__(self,data):
        self.data = data
        self.next  = None
        self.previous = None

    
class DoubleLinkedList:
    def __init__(self):
        self.head = None #first node
        self.tail = None #last node
        
    def insert(self, data):
        """
        Inserting data to the end off the linkedList
        """
        new_node = Node(data)

        if self.head is None:
            # We are checking  if the linkedList is not empty
            # if it is empty the new added node will be the head
            self.head = new_node
        else:
            # When we have a head data that means we will make 
            # the new added data previous pointer to point to the tail
            new_node.previous = self.tail
            # then make the tail next node to point to the new  added node
            self.tail.next = new_node
            # then replace the tail node to be the last node
            self.tail = new_node

    # we can travers double linkedList in both direction
    def traverse_forward(self):
        # we will keep trackof the first node
        actual_node = self.head

        # the last node next pointeris None
        # we will keep moving forward until we touch the last node
        while actual_node is not  None:
            actual_node = actual_node.next
        
    def traverse_backward(self):
        # we will keep trackof the last node
        actual_node = self.tail

        # the last node previous pointer is None
        # we will keep moving backward until we touch the last node
        while actual_node is not  None:
            actual_node = actual_node.previous

if __name__ == '__main__':
    
    linked_list = DoubleLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    # 1 2 3
    linked_list.traverse_forward()

    # 3 2 1
    linked_list.traverse_backward()