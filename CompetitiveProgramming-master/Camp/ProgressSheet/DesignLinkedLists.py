class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

 
    def get(self, index: int) -> int:
        if self.head == self.tail == None:
            return -1
    
        else:
            current = self.head
            for _ in range(index):
                if current != None:
                    current = current.next

        return current.value if current != None else -1

    def addAtHead(self, val: int) -> None:
        obj = Node(val)

        if self.head == self.tail == None :
            obj.next = self.head
            self.tail = self.head = obj
        else:
            obj.next = self.head
            self.head = obj


    def addAtTail(self, val: int) -> None:
        obj = Node(val)

        if self.head == self.tail == None :
            obj.next = self.tail
            self.tail = self.head = obj
        else:
            obj.next = None
            self.tail.next = obj
            self.tail = obj

    def addAtIndex(self, index: int, val: int) -> None:
        obj = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for _ in range(index-1):
                if current != None:
                    current = current.next

            if current != None:
                obj.next = current.next
                current.next = obj 
                
                if obj.next == None:
                    self.tail = obj
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head == self.tail == None:
            print("List is empty")
        elif index == 0:
            self.head = self.head.next

            if self.head and self.head.next == None:
                self.head == self.tail
        else: 
            current = self.head
            for _ in range(index-1):
                if current != None:
                    current = current.next

            if (current != None) and (current.next != None):
                current.next = current.next.next
                if current.next == None:
                    self.tail = current

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)