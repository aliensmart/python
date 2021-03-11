class Node:
    """
        Each Node has data and a pointer, when there is no next node the pointer will be null
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        """
        When we first instanciate the linkedList  class we don't have anydata we have empty.
        """
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self,  data):
        """
        We are always inserting at the beginning of the linkedList so we will always checjk if the there is not a node
        if a node exist we will put the new node as the head and put the head as the next node
        """
        self.num_of_nodes += 1
        new_node = Node(data)

# if  the head is not we will add the new node as the head
        if not self.head:
            self.head = new_node 

        # if there  is head we will point the new node next node  to the existing heead  and  the new node will become the head
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        """

        """
        self.num_of_nodes += 1
        # We first store the new node in a variable 
        new_node = Node(data)

        
        actual_node = self.traverse()

        # then we point the actual node next node to the data we will store
        actual_node.next_node = new_node


    def size(self):
        return self.num_of_nodes

    def traverse(self):
        # and we get the head of the linkedList and store it in the actual_node variable
        actual_node = self.head

        #We loop  through all node and  check if there is a next nod
        # oncewe don't have a next  node we will  change the actual_node to the last node of the  linkedList
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        return actual_node

    
    def remove(self, data):

        if self.head is None:
            return
        
        # We store the head in the actual node variable as the is the only node we always have access
        actual_node = self.head

        # We create a previous node to be able to store the last node we leave
        # to  be able to reconnect the nodes when we delete the data
        previous_node = None
        
        #  We will first check if the actual node exist(the head node)
        #  And if the actual  node is does not have the data we  want to delete

        while actual_node is not None and  actual_node.data != data:
            # Once we loop through all node 
            # the previous node becomes the node we just moved on with 
            previous_node = actual_node

            # and the actual node become the next node
            actual_node = actual_node.next_node

        # do nothing when the actual node is empty
        if actual_node is None:
            return

        # if we found the data and the previous 
        # node is none that mean we have removed 
        # the head so we have to point the new 
        # head to the delete node next node pointer
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # if we have the previous node we will point the 
            # next node to the deleted node next node pointer
            previous_node.next_node = actual_node.next_node



    
