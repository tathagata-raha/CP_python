

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def deleteNode(self, key):  # Deleting a node with a key
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
            
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return
        prev.next = temp.next
        
    def deletePos(self, position):
        if self.head == None:
            return
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
 
        temp.next = next
        
    def getLength(self):
        temp = self.head 
        count = 0 
        while (temp):
            count += 1
            temp = temp.next
        return count
        
    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
             
            current = current.next
        return False
        
    def getNth(self, index):
        current = self.head
        count = 0
        
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        return None
        
    def printLinkedList(self):
        tmp = self.head
        print("Linked List:", end=' ')
        while tmp.next is not None:
            print(tmp.data, end = '->')
            tmp = tmp.next
        print(tmp.data)
        
    
ll = LinkedList()
ll.push(12)
ll.push(11)
ll.push(10)
ll.push(9)
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.printLinkedList()
print("Deleting node with key 5")
ll.deleteNode(5)
ll.printLinkedList()

print("Deleting node at 5th position")
ll.deletePos(5)
ll.printLinkedList()

print("Length of LinkedList:",ll.getLength())

print("Searching for element 10:", ll.search(10))

print("Searching for element 5:", ll.search(5))

print("Element at the 5th position:", ll.getNth(5))

# ll.deleteNodePos(5)
# ll.printLinkedList()