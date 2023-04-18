"""
    #1 Push /
    #2 Pop /
    #3 Shift /
    #4 Unshift /
    #5 Get
    #6 Set
    #7 Insert
    #8 Remove
    #9 Reverse
"""

class Node:
    def __init__(self, value):
        self.value = value # int
        self.next = None   # node

class SinglyLinkedList:
    def __init__(self):
        self.length = 0    # int
        self.head = None   # node
        self.tail = None   # node
    
    def push(self, value):
        new_node = Node(value)
        
        if(self.head == None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1
    
    def pop(self):
        if(self.head == None):
            return
        
        before_node = self.head
        after_node = before_node
        
        while after_node.next:
            before_node = after_node
            after_node = after_node.next
            
        before_node.next = None
        self.tail = before_node
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return after_node.value
      
    def print(self):
        current = self.head
        result = ""
        
        while current != None:
            result += f"({current.value}) -> "
            current = current.next
        
        result += "None"
        
        print(result)
    
    def shift(self):
        if self.head == None:
            return
            
        first_node = self.head
        self.head = first_node.next
        self.length -= 1
        
        return first_node.value
    
    def unshift(self, value):
        new_node = Node(value)
        
        new_node.next = self.head
        self.head = new_node
        
SLL = SinglyLinkedList()
SLL.push(1)
SLL.push(2)
SLL.push(3)
SLL.print()
        
"""
    Linked List
    [ None ]
       HT
       
    new_node = [2]
    
    [ [1] -> None ]
      HT
      
    [ [1] -> [2] -> None ]
      H       T
      
    insert(index, value) get()
    [ [1] -> [2] -> [100] -> None -> ]
      H              T
    []
"""