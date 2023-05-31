# /*
#  * 
#  * READ THIS NOTE:
#  * Sir naka python po ako, bali pa palitan nalang po ng extension .java to .py
#  * main.java -> main.py
#  * 
#  * Github Link for CLL: 
#  * https://github.com/BernardSapida/Data_Structure_And_Algorithm/blob/master/Linked%20List/Doubly/Circular/CircularLinkedList.py
#  * 
#  */

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head
        self.finger = self.head
        self.finger_index = -1
        self.size = 0
        
    # add(index, value) -> Add new node to said index
    def insert(self, index, value):
        cur = self.head if (index == self.size) else self.getNodeAt(index)
        newNode = Node()
        newNode.value = value
        newNode.prev = cur.prev
        newNode.next = cur
        newNode.prev.next = newNode
        newNode.next.prev = newNode
        
        self.finger = newNode
        
        if cur == self.head:
            self.finger_index = self.size
        
        self.size += 1
    
    # add(value) -> Add node to last index
    def add(self, value):
        self.insert(self.size, value)
    
    # remove node at index
    def remove(self, index):
        toRemove = self.getNodeAt(index)
        
        if toRemove is None:
            return None
        
        self.finger = toRemove.prev
        self.finger_index -= 1
        
        toRemove.prev.next = toRemove.next
        toRemove.next.prev = toRemove.prev
        toRemove.prev = None
        toRemove.next = None
        
        self.size -= 1
        
        return toRemove.value
    
    # remove node with value of
    def removeValue(self, value):
        index = self.indexOf(value)
        
        if (index == -1):
            return False
        
        self.remove(index)
        return True
    
    # index of node with value of
    def indexOf(self, value):
        itr = self.head.next
        old_finger_index = self.finger_index
        self.finger_index = -1
        i = 0
        
        while itr != self.head:
            self.finger_index += 1
            
            if (itr.value == value):
                self.finger = itr
                return i

            itr = itr.next
            i += 1
        
        self.finger_index = old_finger_index
        return -1
    
    # return True/False if value exists
    def contains(self, value):
        return self.indexOf(value) != -1
    
    # return node value at index
    def get(self, index):
        accessed_node = self.getNodeAt(index)
        
        if accessed_node is None:
            return None
        
        self.finger = accessed_node
        
        return accessed_node.value
    
    # set new value of node at index
    def set(self, index, value):
        cur = self.getNodeAt(index)
        oldValue = cur.value
        cur.value = value
        
        self.finger = cur
        
        return oldValue
    
    # get size of CLL
    def size(self):
        return self.size
    
    # clear all nodes
    def clear(self):
        self.size = 0
        self.head.next = self.head
        self.head.prev = self.head
        self.finger = self.head
        self.finger_index = -1
        
    # return True/False if CLL is empty
    def isEmpty(self):
        return self.size == 0
    
    # return node at index
    def getNodeAt(self, index):
        if (index < 0 or index >= self.size):
            return None

        itr = None
        
        # traverse forward from finger
        if index >= self.finger_index:
            itr = self.finger
            
            # To track if it works perfectly (Uncomment to test)
            # print("FROM FINGER FORWARD INDEX: " + str(self.finger_index))
            for _ in range(self.finger_index, index):
                itr = itr.next
                self.finger_index += 1
                # To track if it works perfectly (Uncomment to test)
                # print("FROM FINGER FORWARD INDEX: " + str(self.finger_index))
         
        # traverse backward from finger
        elif self.finger_index - index <= index:
            itr = self.finger
            
            # To track if it works perfectly (Uncomment to test)
            # print("FROM FINGER BACKWARD INDEX: " + str(self.finger_index))
            for _ in range(self.finger_index, index, -1):
                itr = itr.prev
                self.finger_index -= 1
                # To track if it works perfectly (Uncomment to test)
                # print("FROM FINGER BACKWARD INDEX: " + str(self.finger_index))
                
        # traverse forward from head
        else:
            itr = self.head    
            self.finger_index = -1
            
            # To track if it works perfectly (Uncomment to test)
            # print("FROM HEAD FORWARD INDEX: " + str(self.finger_index))
            for _ in range(index + 1):
                itr = itr.next
                self.finger_index += 1
                # To track if it works perfectly (Uncomment to test)
                # print("FROM HEAD FORWARD INDEX: " + str(self.finger_index))

        return itr
    
    # Visualization of CLL
    def toString(self):
        temp = ""
        current_node = self.head.next
        
        while current_node != self.head:
            temp = temp + ", " + str(current_node.value)
            current_node = current_node.next
            
        return f"[{temp[2:]}]"
    
    # Returns the current index of the finger or -1 
    # if the finger is pointing at the head node.
    def indexOfBookmark(self):
        return self.finger_index
    
    # Returns the element pointed by the finger or null
    # if the finger is pointing at the head node.
    def getBookmark(self):
        return None if self.finger == self.head else self.finger
    
    
CLL = CircularLinkedList()

# Kindly uncomment below to test

# CLL.insert(0, 1) # index: 0
# CLL.insert(1, 2) # index: 1
# CLL.insert(2, 3) # index: 2

# CLL.add(4) # index: 3
# CLL.add(5) # index: 4
# CLL.add(6) # index: 5
# CLL.add(7) # index: 6
# CLL.add(8) # index: 7

# CLL.remove(7)
# CLL.remove(2)

# CLL.removeValue(4)
# CLL.removeValue(5)

# CLL.get(0)
# CLL.get(1)
# CLL.get(2)

# CLL.set(0, 11)
# CLL.set(1, 12)
# CLL.set(2, 13)

# print(CLL.indexOf(4))
# print(CLL.indexOf(5))
# print(CLL.indexOf(6))

# CLL.clear()

print(CLL.toString())

print(f"Finger Index: {CLL.indexOfBookmark()}")

# Finger value is None if CLL is empty
print(f"Finger Value: {CLL.getBookmark().value if CLL.getBookmark() != None else None}")
