# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head:[ListNode]) -> int:
        prev= dummy = ListNode(0,head)
        slow, fast = head, head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        nxt = slow.next
        slow.next = None
        
        while nxt:
            temp = nxt
            nxt = nxt.next
            temp.next = slow
            slow = temp

        max_twin = 0
        head_ptr, slow_ptr = head, slow
        while head_ptr and slow_ptr:
            max_twin = max(max_twin, head_ptr.val + slow_ptr.val)
            head_ptr = head_ptr.next
            slow_ptr = slow_ptr.next

        return max_twin