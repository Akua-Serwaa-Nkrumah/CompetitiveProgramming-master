# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        ptr = dummy

        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next

            ptr = ptr.next

        ptr.next = ptr1 if ptr2 == None else ptr2

        return dummy.next