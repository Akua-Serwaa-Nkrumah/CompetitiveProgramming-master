# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head:[ListNode]) -> [ListNode]:
        prev = dummy = ListNode(0,head)
        current = prev.next

        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            
            if prev.next == current:
                prev = prev.next
            else:
                prev.next = current.next
            
            current = current.next
            
        return dummy.next


        