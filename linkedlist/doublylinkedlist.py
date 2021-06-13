
class Node:
    def __init__(self, data):
        self.next = None # reference to next node in DLL
        self.prev = None # reference to previous node in DLL
        self.data = data
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        new_node = Node(data = new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
 
        if new_node.next is not None:
            new_node.next.prev = new_node
            
    def printLinkedList(self):
        tmp = self.head
        print("Linked List:", end=' ')
        while tmp.next is not None:
            print(tmp.data, end = '->')
            tmp = tmp.next
        print(tmp.data)
            
ll = DoublyLinkedList()
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
# head = push(head, 7)

# head = push(head, 1)

# head = push(head, 4)