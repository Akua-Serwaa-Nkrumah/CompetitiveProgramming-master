class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class MyStack:

    def __init__(self):
        self.head = None

    def push(self, x: int) -> None:
        obj = Node(x)
        obj.next = self.head
        self.head = obj
        

    def pop(self) -> int:
        last = self.head
        self.head = self.head.next
        return last.val
        

    def top(self) -> int:
        return self.head.val 
        

    def empty(self) -> bool:
        return self.head == None 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()