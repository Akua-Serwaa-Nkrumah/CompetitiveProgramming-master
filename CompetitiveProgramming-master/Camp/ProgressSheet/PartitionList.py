# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        small_p = small_dummy = ListNode()

        big_p = big_dummy = ListNode()

        ptr = head

        while ptr:
            if ptr.val < x:
                small_p.next = ptr
                small_p = small_p.next
            else:
                big_p.next = ptr
                big_p = big_p.next

            ptr = ptr.next

        big_p.next = None
        small_p.next = big_dummy.next

        return small_dummy.next
        