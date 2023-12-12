# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        odd_p = oddNode = ListNode()
        even_p = evenNode = ListNode()
        ptr = head

        while ptr:
            odd_p.next = ptr
            odd_p = odd_p.next
            if ptr != None:
                ptr = ptr.next

            even_p.next = ptr
            even_p = even_p.next

            if ptr != None:
                ptr = ptr.next
            

        odd_p.next = evenNode.next

        return oddNode.next
