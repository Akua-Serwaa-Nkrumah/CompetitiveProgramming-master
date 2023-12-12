class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0,head)
        prev = dummy
        current = head
        
        for i in range(1,left):
            current = current.next
            prev = prev.next
        temp = prev.next 
        current = current.next 
        
        for j in range(right-left):
            nxt = current.next
            current.next = temp
            temp = current
            current = nxt
            
        prev.next.next = current 
        prev.next = temp 

        return dummy.next

        