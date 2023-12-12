# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        
        linkedstr = ''
        current = head

        while current:
            linkedstr += str(current.val)
            current = current.next

        
        return list(linkedstr) == list(reversed(linkedstr))


        
        