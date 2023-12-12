class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = Node()
        self.last = Node()
        self.size = 0
  

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False 

        obj = Node(value)

        if self.size == 0:
            self.front = obj
            self.last = obj
        else:
            self.last.next = obj
            self.last = obj
            obj.next = self.front

        self.size += 1
        return True
  

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            self.front = self.front.next

        self.size -= 1
        return True
        

    def Front(self) -> int:
        return self.front.val if self.size != 0 else -1
          

    def Rear(self) -> int:
        return self.last.val if self.size != 0 else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()